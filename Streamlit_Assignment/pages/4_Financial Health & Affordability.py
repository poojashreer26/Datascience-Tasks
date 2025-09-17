# pages/4_Financial_Health.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import final_df
from preprocessing import Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Portfolio Risk - Financial Health", layout="wide")
st.title("📈 Page 4 — Financial Health & Affordability")

# ----------------- Apply Global Filters -----------------
df_filters = Global_filters(final_df)

# Helper: safe column fetch (falls back to zeros / NaNs)
def safe_series(df_filters, col):
    return df_filters[col] if col in df_filters.columns else pd.Series(np.nan, index=df_filters.index)

AMT_INCOME = safe_series(df_filters, "AMT_INCOME_TOTAL")
AMT_CREDIT = safe_series(df_filters, "AMT_CREDIT")
AMT_ANNUITY = safe_series(df_filters, "AMT_ANNUITY")
AMT_GOODS = safe_series(df_filters, "AMT_GOODS_PRICE")
DTI = safe_series(df_filters, "DTI")  # ideally computed in preprocessing
LTI = safe_series(df_filters, "LOAN_TO_INCOME")  # ideally computed in preprocessing
TARGET = safe_series(df_filters, "TARGET")

# Compute derived columns if missing
if DTI.isna().all() and ("AMT_ANNUITY" in df_filters.columns and "AMT_INCOME_TOTAL" in df_filters.columns):
    DTI = AMT_ANNUITY / AMT_INCOME
if LTI.isna().all() and ("AMT_CREDIT" in df_filters.columns and "AMT_INCOME_TOTAL" in df_filters.columns):
    LTI = AMT_CREDIT / AMT_INCOME

# ----------------- KPIs -----------------
st.subheader("📌 KPIs — Financial Health & Affordability")
# safe numeric summary helpers
def mean_safe(s): 
    return float(s.dropna().mean()) if not s.dropna().empty else np.nan
def median_safe(s): 
    return float(s.dropna().median()) if not s.dropna().empty else np.nan
def pct_high(s, thresh):
    return 100.0 * s.dropna().gt(thresh).mean() if not s.dropna().empty else np.nan

kpi_avg_income = mean_safe(AMT_INCOME)
kpi_median_income = median_safe(AMT_INCOME)
kpi_avg_credit = mean_safe(AMT_CREDIT)
kpi_avg_annuity = mean_safe(AMT_ANNUITY)
kpi_avg_goods = mean_safe(AMT_GOODS)
kpi_avg_dti = mean_safe(DTI)
kpi_avg_lti = mean_safe(LTI)

# Income / credit gaps by target (non-def = TARGET==0, def = TARGET==1)
income_non_def = mean_safe(AMT_INCOME[TARGET == 0])
income_def = mean_safe(AMT_INCOME[TARGET == 1])
credit_non_def = mean_safe(AMT_CREDIT[TARGET == 0])
credit_def = mean_safe(AMT_CREDIT[TARGET == 1])
income_gap = income_non_def - income_def if not np.isnan(income_non_def) and not np.isnan(income_def) else np.nan
credit_gap = credit_non_def - credit_def if not np.isnan(credit_non_def) and not np.isnan(credit_def) else np.nan

pct_high_credit = pct_high(AMT_CREDIT, 1_000_000)

# Layout KPIs in 5 columns (two metrics each)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Avg Annual Income", f"{kpi_avg_income:,.0f}" if not np.isnan(kpi_avg_income) else "N/A")
    st.metric("Median Annual Income", f"{kpi_median_income:,.0f}" if not np.isnan(kpi_median_income) else "N/A")
with col2:
    st.metric("Avg Credit Amount", f"{kpi_avg_credit:,.0f}" if not np.isnan(kpi_avg_credit) else "N/A")
    st.metric("Avg Annuity", f"{kpi_avg_annuity:,.0f}" if not np.isnan(kpi_avg_annuity) else "N/A")
with col3:
    st.metric("Avg Goods Price", f"{kpi_avg_goods:,.0f}" if not np.isnan(kpi_avg_goods) else "N/A")
    st.metric("Avg DTI", f"{kpi_avg_dti:.3f}" if not np.isnan(kpi_avg_dti) else "N/A")
with col4:
    st.metric("Avg LTI", f"{kpi_avg_lti:.3f}" if not np.isnan(kpi_avg_lti) else "N/A")
    st.metric("Income Gap (Non-def − Def)", f"{income_gap:,.0f}" if not np.isnan(income_gap) else "N/A")
with col5:
    st.metric("Credit Gap (Non-def − Def)", f"{credit_gap:,.0f}" if not np.isnan(credit_gap) else "N/A")
    st.metric("% High Credit (>1M)", f"{pct_high_credit:.2f}%" if not np.isnan(pct_high_credit) else "N/A")

st.divider()

# ----------------- Charts -----------------
st.subheader("📊 Financial Distributions & Relationships")
# Helper to trim extremes (99th percentile) for plotting
def trim99(series):
    q = series.dropna().quantile(0.99)
    return series.clip(upper=q)

# 1. Histogram — Income distribution
st.markdown("### 💰 Histogram — Annual Income")
fig, ax = plt.subplots()
sns.histplot(trim99(AMT_INCOME).dropna(), bins=60, kde=True, ax=ax)
ax.set_xlabel("AMT_INCOME_TOTAL (trimmed at 99th pct)")
st.pyplot(fig)

# 2. Histogram — Credit distribution
st.markdown("### 🏦 Histogram — Credit Amount")
fig, ax = plt.subplots()
sns.histplot(trim99(AMT_CREDIT).dropna(), bins=60, kde=True, ax=ax)
ax.set_xlabel("AMT_CREDIT (trimmed at 99th pct)")
st.pyplot(fig)

# 3. Histogram — Annuity distribution
st.markdown("### 💸 Histogram — Annuity")
fig, ax = plt.subplots()
sns.histplot(trim99(AMT_ANNUITY).dropna(), bins=60, kde=True, ax=ax)
ax.set_xlabel("AMT_ANNUITY (trimmed at 99th pct)")
st.pyplot(fig)

# 4. Scatter — Income vs Credit (alpha blending)
st.markdown("### 🔎 Scatter — Income vs Credit")
fig, ax = plt.subplots(figsize=(8,5))
x = AMT_INCOME.dropna()
y = AMT_CREDIT.reindex(x.index)
ax.scatter(x, y, alpha=0.25, s=8)
ax.set_xlim(0, x.quantile(0.99) if not x.empty else 1)
ax.set_ylim(0, y.quantile(0.99) if not y.empty else 1)
ax.set_xlabel("AMT_INCOME_TOTAL")
ax.set_ylabel("AMT_CREDIT")
st.pyplot(fig)

# 5. Scatter — Income vs Annuity
st.markdown("### 🔎 Scatter — Income vs Annuity")
fig, ax = plt.subplots(figsize=(8,5))
x2 = AMT_INCOME.dropna()
y2 = AMT_ANNUITY.reindex(x2.index)
ax.scatter(x2, y2, alpha=0.25, s=8)
ax.set_xlim(0, x2.quantile(0.99) if not x2.empty else 1)
ax.set_ylim(0, y2.quantile(0.99) if not y2.empty else 1)
ax.set_xlabel("AMT_INCOME_TOTAL")
ax.set_ylabel("AMT_ANNUITY")
st.pyplot(fig)

# 6. Boxplot — Credit by Target
st.markdown("### 📦 Boxplot — Credit by Target")
fig, ax = plt.subplots(figsize=(8,4))
if "AMT_CREDIT" in df_filters.columns and "TARGET" in df_filters.columns:
    sns.boxplot(x="TARGET", y="AMT_CREDIT", data=df_filters, ax=ax)
    ax.set_ylim(0, df_filters["AMT_CREDIT"].dropna().quantile(0.99))
else:
    ax.text(0.5, 0.5, "Required columns missing", ha="center")
st.pyplot(fig)

# 7. Boxplot — Income by Target
st.markdown("### 📦 Boxplot — Income by Target")
fig, ax = plt.subplots(figsize=(8,4))
if "AMT_INCOME_TOTAL" in df_filters.columns and "TARGET" in df_filters.columns:
    sns.boxplot(x="TARGET", y="AMT_INCOME_TOTAL", data=df_filters, ax=ax)
    ax.set_ylim(0, df_filters["AMT_INCOME_TOTAL"].dropna().quantile(0.99))
else:
    ax.text(0.5, 0.5, "Required columns missing", ha="center")
st.pyplot(fig)

# 8. KDE / Density — Joint Income–Credit
st.markdown("### 🧭 KDE — Joint Income vs Credit Density")
fig, ax = plt.subplots(figsize=(7,6))
if not AMT_INCOME.dropna().empty and not AMT_CREDIT.dropna().empty:
    sns.kdeplot(x=trim99(AMT_INCOME).dropna(), y=trim99(AMT_CREDIT).dropna(), fill=True, thresh=0.05, ax=ax)
    ax.set_xlim(0, AMT_INCOME.dropna().quantile(0.99))
    ax.set_ylim(0, AMT_CREDIT.dropna().quantile(0.99))
else:
    ax.text(0.5, 0.5, "Insufficient data for KDE", ha="center")
st.pyplot(fig)

# 9. Bar — Income Brackets vs Default Rate
st.markdown("### 📊 Bar — Income Brackets vs Default Rate")
if "INCOME_BRACKET" in df_filters.columns and "TARGET" in df_filters.columns:
    br = df_filters.groupby("INCOME_BRACKET")["TARGET"].mean().sort_index() * 100
    fig, ax = plt.subplots()
    sns.barplot(x=br.index.astype(str), y=br.values, ax=ax)
    ax.set_ylabel("Default Rate (%)")
    ax.set_xlabel("Income Bracket")
    st.pyplot(fig)
else:
    st.info("INCOME_BRACKET not found in dataframe — create it in preprocessing (e.g., qcut of AMT_INCOME_TOTAL).")

# 10. Heatmap — Financial variable correlations
st.markdown("### 🔥 Heatmap — Financial Correlations")
fin_cols = []
for col in ["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "DTI", "LOAN_TO_INCOME", "TARGET"]:
    if col in df_filters.columns:
        fin_cols.append(col)
# If LOAN_TO_INCOME exists under other name:
if "LOAN_TO_INCOME" not in fin_cols and "LOAN_TO_INCOME" in df_filters.columns:
    fin_cols.append("LOAN_TO_INCOME")

if fin_cols:
    corr = df_filters[fin_cols].corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="vlag", center=0, ax=ax)
    st.pyplot(fig)
else:
    st.info("Not enough financial columns present to compute heatmap.")

st.divider()

# ----------------- Affordability thresholds & narrative -----------------
st.subheader("📝 Affordability Thresholds & Narrative")

LTI_threshold = st.number_input("LTI threshold (loan-to-income) to test", value=6.0, step=0.5)
DTI_threshold = st.number_input("DTI threshold (annuity/income) to test", value=0.35, step=0.01)

# compute default rates above thresholds
def default_rate_for_mask(mask):
    if mask.sum() == 0 or "TARGET" not in df_filters.columns:
        return np.nan, 0
    rate = df_filters.loc[mask, "TARGET"].mean() * 100
    return rate, int(mask.sum())

mask_lti = (LTI > LTI_threshold)
mask_dti = (DTI > DTI_threshold)
mask_both = mask_lti & mask_dti

lti_rate, lti_n = default_rate_for_mask(mask_lti)
dti_rate, dti_n = default_rate_for_mask(mask_dti)
both_rate, both_n = default_rate_for_mask(mask_both)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(f"Default Rate LTI > {LTI_threshold}", f"{lti_rate:.2f}%" if not np.isnan(lti_rate) else "N/A", delta=f"{lti_n} cases")
with col_b:
    st.metric(f"Default Rate DTI > {DTI_threshold}", f"{dti_rate:.2f}%" if not np.isnan(dti_rate) else "N/A", delta=f"{dti_n} cases")
with col_c:
    st.metric(f"Default Rate (both)", f"{both_rate:.2f}%" if not np.isnan(both_rate) else "N/A", delta=f"{both_n} cases")

st.markdown("---")
# Narrative / simple insights
insights = []
overall_def_rate = df_filters["TARGET"].mean() * 100 if "TARGET" in df_filters.columns else np.nan
if not np.isnan(overall_def_rate):
    insights.append(f"- **Overall default rate:** {overall_def_rate:.2f}% (used as baseline).")

if not np.isnan(lti_rate):
    insights.append(f"- **LTI > {LTI_threshold}:** default rate = {lti_rate:.2f}% (n={lti_n}). {'Higher' if lti_rate>overall_def_rate else 'Lower or similar'} than baseline.")
else:
    insights.append("- **LTI analysis:** insufficient data.")

if not np.isnan(dti_rate):
    insights.append(f"- **DTI > {DTI_threshold}:** default rate = {dti_rate:.2f}% (n={dti_n}). {'Higher' if dti_rate>overall_def_rate else 'Lower or similar'} than baseline.")
else:
    insights.append("- **DTI analysis:** insufficient data.")

if not np.isnan(both_rate):
    insights.append(f"- **Both thresholds:** default rate = {both_rate:.2f}% (n={both_n}).")
else:
    insights.append("- **Combined LTI & DTI:** insufficient data.")

# Show insights
for line in insights:
    st.markdown(line)

st.markdown("""
**Suggested next steps**
- Validate LTI/DTI behavior across income brackets (e.g., higher LTI may matter more for low-income applicants).
- Consider building a simple binned risk table: income bracket × LTI band → default rate.
- If certain bins have very high default rates and adequate sample size, flag them for stricter underwriting.
""")
