# pages/5_Correlations_Drivers.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import final_df
from preprocessing import Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Portfolio Risk - Correlations & Drivers", layout="wide")
st.title("🔍 Page 5 — Correlations, Drivers & Interactive Slice-and-Dice")

# ----------------- Apply Global Filters -----------------
df = Global_filters(final_df)

# ----------------- KPIs -----------------
st.subheader("📌 KPIs — Correlations & Drivers")

# Keep only numeric columns
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Correlation matrix
if not num_cols:
    st.warning("No numeric columns available for correlation analysis.")
else:
    corr = df[num_cols].corr()

    # Correlations with TARGET
    if "TARGET" in corr.columns:
        corr_target = corr["TARGET"].drop("TARGET").sort_values(ascending=False)
        top_pos = corr_target.head(5)
        top_neg = corr_target.tail(5)
    else:
        corr_target = pd.Series()
        top_pos, top_neg = pd.Series(), pd.Series()

    # Specific KPIs
    most_corr_income = corr["AMT_INCOME_TOTAL"].drop("AMT_INCOME_TOTAL").abs().sort_values(ascending=False).head(1) \
        if "AMT_INCOME_TOTAL" in corr.columns else pd.Series()
    most_corr_credit = corr["AMT_CREDIT"].drop("AMT_CREDIT").abs().sort_values(ascending=False).head(1) \
        if "AMT_CREDIT" in corr.columns else pd.Series()
    corr_income_credit = corr.loc["AMT_INCOME_TOTAL", "AMT_CREDIT"] \
        if {"AMT_INCOME_TOTAL", "AMT_CREDIT"}.issubset(corr.columns) else np.nan
    corr_age_target = corr.loc["AGE_YEARS", "TARGET"] if {"AGE_YEARS", "TARGET"}.issubset(corr.columns) else np.nan
    corr_emp_target = corr.loc["Employe worked", "TARGET"] if {"Employe worked", "TARGET"}.issubset(corr.columns) else np.nan
    corr_family_target = corr.loc["CNT_FAM_MEMBERS", "TARGET"] if {"CNT_FAM_MEMBERS", "TARGET"}.issubset(corr.columns) else np.nan

    # Variance explained (proxy)
    var_explained = corr_target.abs().nlargest(5).sum() if not corr_target.empty else np.nan
    strong_corr_features = (corr.abs() > 0.5).sum().sum() // 2  # upper triangle approx

    # Display KPIs in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Top +Corr (TARGET)", ", ".join([f"{k}:{v:.2f}" for k,v in top_pos.items()]) if not top_pos.empty else "N/A")
        st.metric("Top -Corr (TARGET)", ", ".join([f"{k}:{v:.2f}" for k,v in top_neg.items()]) if not top_neg.empty else "N/A")
    with col2:
        st.metric("Most Corr with Income", f"{most_corr_income.index[0]}:{most_corr_income.values[0]:.2f}" if not most_corr_income.empty else "N/A")
        st.metric("Most Corr with Credit", f"{most_corr_credit.index[0]}:{most_corr_credit.values[0]:.2f}" if not most_corr_credit.empty else "N/A")
    with col3:
        st.metric("Corr(Income, Credit)", f"{corr_income_credit:.2f}" if not np.isnan(corr_income_credit) else "N/A")
        st.metric("Corr(Age, TARGET)", f"{corr_age_target:.2f}" if not np.isnan(corr_age_target) else "N/A")
    with col4:
        st.metric("Corr(Emp Yrs, TARGET)", f"{corr_emp_target:.2f}" if not np.isnan(corr_emp_target) else "N/A")
        st.metric("Corr(Family Size, TARGET)", f"{corr_family_target:.2f}" if not np.isnan(corr_family_target) else "N/A")
    with col5:
        st.metric("Var Explained Top 5 (|corr|)", f"{var_explained:.2f}" if not np.isnan(var_explained) else "N/A")
        st.metric("# Features |corr|>0.5", str(strong_corr_features))

st.divider()
# ----------------- Graphs -----------------
st.subheader("📊 Graphs — Correlations & Drivers")

# === Group 1: Correlation Overview ===
st.markdown("## 1️⃣ Correlation Overview")

# 1. Heatmap — Correlation (numeric)
st.markdown("### 1. Correlation Heatmap")
fig1, ax1 = plt.subplots(figsize=(10,6))
if not num_cols:
    ax1.text(0.5, 0.5, "No numeric columns", ha="center")
else:
    sns.heatmap(corr, cmap="coolwarm", center=0, ax=ax1)
st.pyplot(fig1)

# 2. Bar — |Correlation| with TARGET
st.markdown("### 2. |Correlation| with TARGET")
fig2, ax2 = plt.subplots(figsize=(8,4))
if "TARGET" in corr.columns:
    corr_target_abs = corr_target.abs().sort_values(ascending=False).head(10)
    sns.barplot(x=corr_target_abs.values, y=corr_target_abs.index, ax=ax2)
    ax2.set_xlabel("|Correlation|")
else:
    ax2.text(0.5, 0.5, "TARGET missing", ha="center")
st.pyplot(fig2)


# === Group 2: Scatter Relationships ===
st.markdown("## 2️⃣ Scatter Relationships")

# 3. Scatter — Age vs Credit
st.markdown("### 3. Age vs Credit (hue=TARGET)")
fig3, ax3 = plt.subplots(figsize=(6,4))
if {"AGE_YEARS","AMT_CREDIT","TARGET"}.issubset(df.columns):
    sns.scatterplot(x="AGE_YEARS", y="AMT_CREDIT", hue="TARGET",
                    alpha=0.5, data=df.sample(min(2000, len(df))), ax=ax3)
else:
    ax3.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig3)

# 4. Scatter — Age vs Income
st.markdown("### 4. Age vs Income (hue=TARGET)")
fig4, ax4 = plt.subplots(figsize=(6,4))
if {"AGE_YEARS","AMT_INCOME_TOTAL","TARGET"}.issubset(df.columns):
    sns.scatterplot(x="AGE_YEARS", y="AMT_INCOME_TOTAL", hue="TARGET",
                    alpha=0.5, data=df.sample(min(2000, len(df))), ax=ax4)
else:
    ax4.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig4)

# 5. Scatter — Employment Years vs TARGET
st.markdown("### 5. Employment Years vs TARGET")
fig5, ax5 = plt.subplots(figsize=(6,4))
if {"Employe worked","TARGET"}.issubset(df.columns):
    sns.stripplot(x="TARGET", y="Employe worked",
                  data=df.sample(min(3000,len(df))),
                  alpha=0.3, jitter=True, ax=ax5)
else:
    ax5.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig5)


# === Group 3: Segment Boxplots ===
st.markdown("## 3️⃣ Segment Boxplots")

# 6. Boxplot — Credit by Education
st.markdown("### 6. Credit by Education")
fig6, ax6 = plt.subplots(figsize=(8,4))
if {"AMT_CREDIT","NAME_EDUCATION_TYPE"}.issubset(df.columns):
    sns.boxplot(x="NAME_EDUCATION_TYPE", y="AMT_CREDIT", data=df, ax=ax6)
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation=30, ha="right")
else:
    ax6.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig6)

# 7. Boxplot — Income by Family Status
st.markdown("### 7. Income by Family Status")
fig7, ax7 = plt.subplots(figsize=(8,4))
if {"AMT_INCOME_TOTAL","NAME_FAMILY_STATUS"}.issubset(df.columns):
    sns.boxplot(x="NAME_FAMILY_STATUS", y="AMT_INCOME_TOTAL", data=df, ax=ax7)
    ax7.set_xticklabels(ax7.get_xticklabels(), rotation=30, ha="right")
else:
    ax7.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig7)


# === Group 4: Multi-Feature Relationships ===
st.markdown("## 4️⃣ Multi-Feature Relationships")

# 8. Pair Plot — Income, Credit, Annuity, TARGET
st.markdown("### 8. Pair Plot — Income, Credit, Annuity, TARGET")
if {"AMT_INCOME_TOTAL","AMT_CREDIT","AMT_ANNUITY","TARGET"}.issubset(df.columns):
    sns.pairplot(df.sample(min(1500,len(df))),
                 vars=["AMT_INCOME_TOTAL","AMT_CREDIT","AMT_ANNUITY"],
                 hue="TARGET", diag_kind="kde")
    st.pyplot(plt.gcf())
else:
    st.info("Missing columns for pair plot")


# === Group 5: Filtered Default Rates ===
st.markdown("## 5️⃣ Filtered Default Rates")

# 9. Default Rate by Gender
st.markdown("### 9. Default Rate by Gender (filtered)")
fig9, ax9 = plt.subplots(figsize=(6,4))
if {"CODE_GENDER","TARGET"}.issubset(df.columns):
    g = df.groupby("CODE_GENDER")["TARGET"].mean().mul(100)
    sns.barplot(x=g.index, y=g.values, ax=ax9)
    ax9.set_ylabel("Default Rate (%)")
else:
    ax9.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig9)

# 10. Default Rate by Education
st.markdown("### 10. Default Rate by Education (filtered)")
fig10, ax10 = plt.subplots(figsize=(8,4))
if {"NAME_EDUCATION_TYPE","TARGET"}.issubset(df.columns):
    e = df.groupby("NAME_EDUCATION_TYPE")["TARGET"].mean().mul(100).sort_values(ascending=False)
    sns.barplot(x=e.values, y=e.index, ax=ax10)
    ax10.set_xlabel("Default Rate (%)")
else:
    ax10.text(0.5,0.5,"Missing cols", ha="center")
st.pyplot(fig10)
