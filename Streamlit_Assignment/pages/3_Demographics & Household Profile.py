# ===================== Page 3: Demographics & Household Profile =====================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import final_df, Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Household Structure & Human Factors", layout="wide")
st.title("📊 Demographics & Household Profile — Page 3")

# ----------------- Apply Global Filters -----------------
df_filtered = Global_filters(final_df)

# ===================== KPIs =====================
st.subheader("📌 Key Demographic & Household KPIs")

# Gender %
gender_counts = df_filtered["CODE_GENDER"].value_counts(normalize=True) * 100
male_pct = gender_counts.get("M", 0)
female_pct = gender_counts.get("F", 0)

# Avg Age by Target
avg_age_defaulters = (df_filtered.loc[df_filtered["TARGET"] == 1, "DAYS_BIRTH"] / -365.25).mean()
avg_age_nondefaulters = (df_filtered.loc[df_filtered["TARGET"] == 0, "DAYS_BIRTH"] / -365.25).mean()

# With children %
with_children_pct = (df_filtered["CNT_CHILDREN"] > 0).mean() * 100

# Avg family size
avg_family_size = df_filtered["CNT_FAM_MEMBERS"].mean()

# Married %
married_pct = (df_filtered["NAME_FAMILY_STATUS"] == "Married").mean() * 100
single_pct = 100 - married_pct

# Higher education %
higher_edu_pct = df_filtered["NAME_EDUCATION_TYPE"].isin(
    ["Higher education", "Academic degree"]
).mean() * 100

# Living with parents %
with_parents_pct = (df_filtered["NAME_HOUSING_TYPE"] == "With parents").mean() * 100

# Currently working %
currently_working_pct = (df_filtered["DAYS_EMPLOYED"] < 0).mean() * 100

# Avg employment years
avg_employment_years = (-df_filtered.loc[df_filtered["DAYS_EMPLOYED"] < 0, "DAYS_EMPLOYED"] / 365.25).mean()

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("👨 % Male", f"{male_pct:.1f}%")
    st.metric("👩 % Female", f"{female_pct:.1f}%")

with col2:
    st.metric("📉 Avg Age (Defaulters)", f"{avg_age_defaulters:.1f} yrs")
    st.metric("📈 Avg Age (Non-Defaulters)", f"{avg_age_nondefaulters:.1f} yrs")

with col3:
    st.metric("👶 % With Children", f"{with_children_pct:.1f}%")
    st.metric("👨‍👩‍👧 Avg Family Size", f"{avg_family_size:.2f}")

with col4:
    st.metric("💍 % Married", f"{married_pct:.1f}%")
    st.metric("🙎 % Single", f"{single_pct:.1f}%")

with col5:
    st.metric("🎓 % Higher Education", f"{higher_edu_pct:.1f}%")
    st.metric("🏠 % Living With Parents", f"{with_parents_pct:.1f}%")
    st.metric("💼 % Currently Working", f"{currently_working_pct:.1f}%")
    st.metric("⏳ Avg Employment Years", f"{avg_employment_years:.1f} yrs")

st.divider()

# ===================== Charts =====================
st.subheader("📊 Visual Insights")

# 1. Histogram — Age Distribution
st.markdown("### 👶 Age Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df_filtered["AGE_YEARS"], bins=30, kde=True, ax=ax1)
st.pyplot(fig1)

# 2. Histogram — Age by Target
st.markdown("### 🎯 Age by Target (Default vs Non-Default)")
fig2, ax2 = plt.subplots()
sns.histplot(df_filtered, x="AGE_YEARS", hue="TARGET", bins=30, kde=True, ax=ax2)
st.pyplot(fig2)

# 3. Bar — Gender distribution
st.markdown("### 🚻 Gender Distribution")
fig3, ax3 = plt.subplots()
sns.countplot(x="CODE_GENDER", data=df_filtered, ax=ax3)
st.pyplot(fig3)

# 4. Bar — Family Status distribution
st.markdown("### 👨‍👩‍👧 Family Status Distribution")
fig4, ax4 = plt.subplots()
sns.countplot(y="NAME_FAMILY_STATUS", data=df_filtered,
              order=df_filtered["NAME_FAMILY_STATUS"].value_counts().index, ax=ax4)
st.pyplot(fig4)

# 5. Bar — Education distribution
st.markdown("### 🎓 Education Distribution")
fig5, ax5 = plt.subplots()
sns.countplot(y="NAME_EDUCATION_TYPE", data=df_filtered,
              order=df_filtered["NAME_EDUCATION_TYPE"].value_counts().index, ax=ax5)
st.pyplot(fig5)

# 6. Bar — Occupation distribution (top 10)
st.markdown("### 💼 Occupation Distribution (Top 10)")
fig6, ax6 = plt.subplots(figsize=(8,5))
occupation_counts = df_filtered["OCCUPATION_TYPE"].value_counts().head(10)
sns.barplot(x=occupation_counts.values, y=occupation_counts.index, ax=ax6)
st.pyplot(fig6)

# 7. Pie — Housing Type distribution
st.markdown("### 🏠 Housing Type Distribution")
fig7, ax7 = plt.subplots()
housing_counts = df_filtered["NAME_HOUSING_TYPE"].value_counts()
ax7.pie(housing_counts, labels=housing_counts.index, autopct="%1.1f%%", startangle=90, wedgeprops=dict(width=0.4))
ax7.axis("equal")
st.pyplot(fig7)

# 8. Countplot — CNT_CHILDREN
st.markdown("### 👶 Number of Children Distribution")
fig8, ax8 = plt.subplots()
sns.countplot(x="CNT_CHILDREN", data=df_filtered, ax=ax8)
st.pyplot(fig8)

# 9. Boxplot — Age vs Target
st.markdown("### 📦 Age vs Target")
fig9, ax9 = plt.subplots()
sns.boxplot(x="TARGET", y="AGE_YEARS", data=df_filtered, ax=ax9)
ax9.set_xticklabels(["Repaid", "Default"])
st.pyplot(fig9)

# 10. Heatmap — Correlation
st.markdown("### 🔥 Correlation Heatmap")
fig10, ax10 = plt.subplots(figsize=(6,4))
corr_vars = df_filtered[["AGE_YEARS", "CNT_CHILDREN", "CNT_FAM_MEMBERS", "TARGET"]].corr()
sns.heatmap(corr_vars, annot=True, cmap="coolwarm", ax=ax10)
st.pyplot(fig10)

st.divider()

# ===================== Narrative Insights =====================
st.subheader("📝 Key Insights")
st.markdown("""
- **Younger applicants** tend to show slightly higher default risk compared to older groups.  
- **Family size & children** correlate with higher credit demand but not always with higher default.  
- **Married applicants** and those with stable housing (own house) tend to show lower risk.  
- **Higher education** applicants generally fall in lower-risk categories.  
- Employment stability (more years worked) correlates with repayment reliability.  
""")
