# pages/2_Target_Risk_Segmentation.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import final_df
from preprocessing import Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Portfolio Risk - Target & Segments", layout="wide")
st.title("🎯 Page 2 — Target & Risk Segmentation")

# ----------------- Apply Global Filters -----------------
df_filters = Global_filters(final_df)

# Safe helpers
def safe_col(df_filters, name, default=np.nan):
    return df_filters[name] if name in df_filters.columns else pd.Series(default, index=df_filters.index)

TARGET = safe_col(df_filters, "TARGET")
AMT_INCOME = safe_col(df_filters, "AMT_INCOME_TOTAL")
AMT_CREDIT = safe_col(df_filters, "AMT_CREDIT")
AMT_ANNUITY = safe_col(df_filters, "AMT_ANNUITY")
AGE = safe_col(df_filters, "AGE_YEARS")
EMP_YEARS = safe_col(df_filters, "Employe worked")  # name used in your preprocessing
# fallback: if Employe worked doesn't exist, compute from DAYS_EMPLOYED
if EMP_YEARS.isna().all() and "DAYS_EMPLOYED" in df_filters.columns:
    EMP_YEARS = df_filters["DAYS_EMPLOYED"].apply(lambda x: x / -365.25 if (not pd.isna(x) and x <= 0) else np.nan)

# Categorical columns used
GENDER = "CODE_GENDER"
EDUC = "NAME_EDUCATION_TYPE"
FAMILY = "NAME_FAMILY_STATUS"
HOUSING = "NAME_HOUSING_TYPE"
CONTRACT = "NAME_CONTRACT_TYPE"

# ----------------- KPIs -----------------
st.subheader("📌 KPIs — Target & Segmentation")

def mean_if_target(col, t):
    if col is None or col.dropna().empty or "TARGET" not in df_filters.columns:
        return np.nan
    s = col[df_filters["TARGET"] == t].dropna()
    return float(s.mean()) if not s.empty else np.nan

total_defaults = int(df_filters["TARGET"].sum()) if "TARGET" in df_filters.columns else 0
default_rate = float(df_filters["TARGET"].mean() * 100) if "TARGET" in df_filters.columns else np.nan

# Default rate by categorical groups (as percentages)
def_pct_gender = df_filters.groupby(GENDER)["TARGET"].mean().mul(100) if GENDER in df_filters.columns else pd.Series()
def_pct_educ = df_filters.groupby(EDUC)["TARGET"].mean().mul(100) if EDUC in df_filters.columns else pd.Series()
def_pct_family = df_filters.groupby(FAMILY)["TARGET"].mean().mul(100) if FAMILY in df_filters.columns else pd.Series()
def_pct_housing = df_filters.groupby(HOUSING)["TARGET"].mean().mul(100) if HOUSING in df_filters.columns else pd.Series()

avg_income_def = mean_if_target(AMT_INCOME, 1)
avg_credit_def = mean_if_target(AMT_CREDIT, 1)
avg_annuity_def = mean_if_target(AMT_ANNUITY, 1)
avg_employ_years_def = mean_if_target(EMP_YEARS, 1)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Defaults", f"{total_defaults:,}")
    st.metric("Default Rate (%)", f"{default_rate:.2f}%" if not np.isnan(default_rate) else "N/A")
with col2:
    # show top gender default or N/A
    g_val = f"{def_pct_gender.mean():.2f}%" if not def_pct_gender.empty else "N/A"
    st.metric("Default Rate by Gender (avg)", g_val)
    st.metric("Default Rate by Education (avg)", f"{def_pct_educ.mean():.2f}%" if not def_pct_educ.empty else "N/A")
with col3:
    st.metric("Default Rate by Family (avg)", f"{def_pct_family.mean():.2f}%" if not def_pct_family.empty else "N/A")
    st.metric("Default Rate by Housing (avg)", f"{def_pct_housing.mean():.2f}%" if not def_pct_housing.empty else "N/A")
with col4:
    st.metric("Avg Income — Defaulters", f"{avg_income_def:,.0f}" if not np.isnan(avg_income_def) else "N/A")
    st.metric("Avg Credit — Defaulters", f"{avg_credit_def:,.0f}" if not np.isnan(avg_credit_def) else "N/A")
with col5:
    st.metric("Avg Annuity — Defaulters", f"{avg_annuity_def:,.0f}" if not np.isnan(avg_annuity_def) else "N/A")
    st.metric("Avg Employment (yrs) — Defaulters", f"{avg_employ_years_def:.2f}" if not np.isnan(avg_employ_years_def) else "N/A")

st.divider()
# ----------------- Graphs -----------------
st.subheader("📊 Graphs — Target & Risk Segmentation")

# === Group 1: Overall Target Distribution ===
st.markdown("## 1️⃣ Target Distribution")

# 1. Bar — Counts: Default vs Repaid
st.markdown("### 1. Default vs Repaid (Counts)")
fig1, ax1 = plt.subplots(figsize=(6,4))
sns.countplot(x="TARGET", data=df_filters, ax=ax1)
ax1.set_xticklabels(["Repaid (0)", "Defaulted (1)"])
st.pyplot(fig1)


# === Group 2: Default % by Segments ===
st.markdown("## 2️⃣ Default Rates by Segments")

# 2. Bar — Default % by Gender
st.markdown("### 2. Default % by Gender")
fig2, ax2 = plt.subplots(figsize=(6,4))
g = df_filters.groupby("CODE_GENDER")["TARGET"].mean().mul(100)
sns.barplot(x=g.index, y=g.values, ax=ax2)
ax2.set_ylabel("Default Rate (%)")
st.pyplot(fig2)

# 3. Bar — Default % by Education
st.markdown("### 3. Default % by Education")
fig3, ax3 = plt.subplots(figsize=(8,4))
e = df_filters.groupby("NAME_EDUCATION_TYPE")["TARGET"].mean().mul(100).sort_values(ascending=False)
sns.barplot(x=e.values, y=e.index, ax=ax3)
ax3.set_xlabel("Default Rate (%)")
st.pyplot(fig3)

# 4. Bar — Default % by Family Status
st.markdown("### 4. Default % by Family Status")
fig4, ax4 = plt.subplots(figsize=(8,4))
f = df_filters.groupby("NAME_FAMILY_STATUS")["TARGET"].mean().mul(100).sort_values(ascending=False)
sns.barplot(x=f.values, y=f.index, ax=ax4)
ax4.set_xlabel("Default Rate (%)")
st.pyplot(fig4)

# 5. Bar — Default % by Housing Type
st.markdown("### 5. Default % by Housing Type")
fig5, ax5 = plt.subplots(figsize=(8,4))
h = df_filters.groupby("NAME_HOUSING_TYPE")["TARGET"].mean().mul(100).sort_values(ascending=False)
sns.barplot(x=h.values, y=h.index, ax=ax5)
ax5.set_xlabel("Default Rate (%)")
st.pyplot(fig5)


# === Group 3: Distributions by Target ===
st.markdown("## 3️⃣ Distributions by Target")

# 6. Boxplot — Income by Target
st.markdown("### 6. Income by Target")
fig6, ax6 = plt.subplots(figsize=(6,4))
sns.boxplot(x="TARGET", y="AMT_INCOME_TOTAL", data=df_filters, ax=ax6)
ax6.set_xticklabels(["Repaid (0)", "Defaulted (1)"])
st.pyplot(fig6)

# 7. Boxplot — Credit by Target
st.markdown("### 7. Credit by Target")
fig7, ax7 = plt.subplots(figsize=(6,4))
sns.boxplot(x="TARGET", y="AMT_CREDIT", data=df_filters, ax=ax7)
ax7.set_xticklabels(["Repaid (0)", "Defaulted (1)"])
st.pyplot(fig7)

# 8. Violin — Age vs Target
st.markdown("### 8. Age vs Target")
fig8, ax8 = plt.subplots(figsize=(6,4))
sns.violinplot(x="TARGET", y="AGE_YEARS", data=df_filters, ax=ax8, inner="quartile")
ax8.set_xticklabels(["Repaid (0)", "Defaulted (1)"])
st.pyplot(fig8)

# 9. Histogram — Employment Years by Target
st.markdown("### 9. Employment Years by Target")
fig9, ax9 = plt.subplots(figsize=(6,4))
sns.histplot(data=df_filters, x="Employe worked", hue="TARGET",
             element="step", multiple="stack", bins=30, ax=ax9)
st.pyplot(fig9)


# === Group 4: Contract Type vs Target ===
st.markdown("## 4️⃣ Contract Analysis")

# 10. Stacked Bar — Contract Type vs Target
st.markdown("### 10. Contract Type vs Target")
fig10, ax10 = plt.subplots(figsize=(6,4))
c = df_filters.groupby(["NAME_CONTRACT_TYPE","TARGET"]).size().unstack(fill_value=0)
c.plot(kind="bar", stacked=True, ax=ax10)
ax10.set_ylabel("Count")
st.pyplot(fig10)

st.markdown("---")
# Propose hypotheses for top-high and top-low segments (generic examples)
st.markdown("**Proposed hypotheses (examples)**")
st.markdown("""
- Segment(s) with **highest** default rates may combine **low income** and **high LTI / DTI** — examine AMT_INCOME_TOTAL, LOAN_TO_INCOME, and DTI in these groups.
- Higher defaults for some **education/family** categories may reflect different employment stability or application channel differences — check `Employe worked` and contract type.
- **Housing** types with elevated defaults may indicate unstable tenure or informal addresses that correlate with repayment risk.
- **Lowest** default groups often show higher income, lower LTI, longer employment tenure — validate by comparing averages across these segments.
""")

# Optional: show small diagnostic table for the top 3 highest default groups across Education (if present)
if EDUC in df_filters.columns and "TARGET" in df_filters.columns:
    st.markdown("#### Diagnostic table — Education groups (defaults, counts, avg income, avg LTI if present)")
    ed_summary = df_filters.groupby(EDUC).agg(
        default_rate = ("TARGET", "mean"),
        count = ("TARGET", "count"),
        avg_income = ("AMT_INCOME_TOTAL", "mean"),
        avg_credit = ("AMT_CREDIT", "mean"),
        avg_annuity = ("AMT_ANNUITY", "mean")
    ).sort_values("default_rate", ascending=False)
    st.dataframe(ed_summary.round(4))

st.markdown("""
**Suggested next steps**
- Drill into the top-high default segments and compute cross-tabs with `INCOME_BRACKET`, `LOAN_TO_INCOME` and `DTI`.
- Validate sample sizes before concluding (avoid making decisions on tiny groups).
- Build simple binned models or decision rules (income bracket + employment years + contract type) to test discriminatory power.
""")
