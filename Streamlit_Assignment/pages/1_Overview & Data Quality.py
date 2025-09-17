import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import final_df
from utils.dataset import load_data
from preprocessing import Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Portfolio Risk - Overview", layout="wide")
st.title("📊 Portfolio Risk Dashboard — Page 1: Overview & Data Quality")



# ----------------- Apply Global Filters -----------------

df_filtered =Global_filters(final_df)

# ----------------- KPIs -----------------
st.subheader("📈 Key Performance Indicators (KPIs)")

# Compute KPIs
total_applicants = df_filtered["SK_ID_CURR"].nunique()
default_rate = df_filtered["TARGET"].mean() * 100
repaid_rate = 100 - default_rate
total_features = df_filtered.shape[1]
avg_missing_per_feature = df_filtered.isna().mean().mean() * 100
num_features = df_filtered.select_dtypes(include=np.number).shape[1]
cat_features = df_filtered.select_dtypes(exclude=np.number).shape[1]
median_age = df_filtered["AGE_YEARS"].median()
median_income = df_filtered["AMT_INCOME_TOTAL"].median()
avg_credit = df_filtered["AMT_CREDIT"].mean()

# Display in columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👥 Total Applicants", f"{total_applicants:,}")
    st.metric("📉 Default Rate (%)", f"{default_rate:.2f}%")

with col2:
    st.metric("📈 Repaid Rate (%)", f"{repaid_rate:.2f}%")
    st.metric("🔢 Total Features", f"{total_features}")

with col3:
    st.metric("❓ Avg Missing per Feature (%)", f"{avg_missing_per_feature:.2f}%")
    st.metric("⚙️ Features Split", f"{num_features} Num / {cat_features} Cat")

with col4:
    st.metric("👶 Median Age", f"{median_age:.1f} yrs")
    st.metric("💰 Median Annual Income", f"{median_income:,.0f}")

with col5:
    st.metric("🏦 Avg Credit Amount", f"{avg_credit:,.0f}")


col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("👥 Total Applicants", f"{total_applicants:,}")
    st.metric("📉 Default Rate (%)", f"{default_rate:.2f}%")
    
with col2:
    st.metric("📈 Repaid Rate (%)", f"{repaid_rate:.2f}%")
    st.metric("🔢 Total Features", f"{total_features}")
with col3:
    st.metric("❓ Avg Missing (%)", f"{avg_missing_per_feature:.2f}%")
    st.metric("⚙️ Features", f"{num_features} Num / {cat_features} Cat")
with col4:
    st.metric("👶 Median Age", f"{median_age:.1f} yrs")
    st.metric("💰 Median Income", f"{median_income:,.0f}")
with col5:
    st.metric("🏦 Avg Credit Amount", f"{avg_credit:,.0f}")

st.divider()

# ----------------- Graphs -----------------
st.subheader("📊 Graphs — Overview & Data Quality")

# === Group 1: Target Distribution ===
st.markdown("## 1️⃣ Portfolio Risk")
col1_1,col2_2=st.columns(2)
# 1. Pie / Donut — Target distribution
st.markdown("### 1. Target Distribution (Defaults vs Repaid)")
with col1_1:
    fig1, ax1 = plt.subplots(figsize=(2.5,2.5))
    df_filtered["TARGET"].value_counts().plot.pie(
        labels=["Repaid (0)", "Defaulted (1)"],
        autopct="%.1f%%", startangle=90, ax=ax1,
        wedgeprops={"width":0.2}  # makes donut
    )
    ax1.set_ylabel("")
    st.pyplot(fig1)

with col2_2:
# === Group 2: Data Quality ===
    st.markdown("## 2️⃣ Data Quality Checks")

# 2. Bar — Top 20 features by missing %
    st.markdown("### 2. Missing Values by Feature (Top 20)")
    missing = df_filtered.isnull().mean().mul(100).sort_values(ascending=False).head(20)
    fig2, ax2 = plt.subplots(figsize=(8,4))
    sns.barplot(x=missing.values, y=missing.index, ax=ax2)
    ax2.set_xlabel("% Missing")
    st.pyplot(fig2)


# === Group 3: Key Numeric Distributions ===
st.markdown("## 3️⃣ Numeric Feature Distributions")

# 3. Histogram — AGE_YEARS
st.markdown("### 3. Age Distribution")
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.histplot(df_filtered["AGE_YEARS"], bins=30, kde=False, ax=ax3)
ax3.set_xlabel("Age (Years)")
st.pyplot(fig3)

# 4. Histogram — AMT_INCOME_TOTAL
st.markdown("### 4. Annual Income Distribution")
fig4, ax4 = plt.subplots(figsize=(6,4))
sns.histplot(df_filtered["AMT_INCOME_TOTAL"], bins=40, kde=False, ax=ax4)
ax4.set_xlabel("Annual Income")
st.pyplot(fig4)

# 5. Histogram — AMT_CREDIT
st.markdown("### 5. Credit Amount Distribution")
fig5, ax5 = plt.subplots(figsize=(6,4))
sns.histplot(df_filtered["AMT_CREDIT"], bins=40, kde=False, ax=ax5)
ax5.set_xlabel("Credit Amount")
st.pyplot(fig5)


# === Group 4: Boxplots for Outlier Detection ===
st.markdown("## 4️⃣ Outlier Detection")

# 6. Boxplot — AMT_INCOME_TOTAL
st.markdown("### 6. Income (Boxplot)")
fig6, ax6 = plt.subplots(figsize=(6,4))
sns.boxplot(x=df_filtered["AMT_INCOME_TOTAL"], ax=ax6)
st.pyplot(fig6)

# 7. Boxplot — AMT_CREDIT
st.markdown("### 7. Credit Amount (Boxplot)")
fig7, ax7 = plt.subplots(figsize=(6,4))
sns.boxplot(x=df_filtered["AMT_CREDIT"], ax=ax7)
st.pyplot(fig7)


# === Group 5: Categorical Distributions ===
st.markdown("## 5️⃣ Categorical Feature Distributions")

# 8. Countplot — Gender
st.markdown("### 8. Gender Distribution")
fig8, ax8 = plt.subplots(figsize=(6,4))
sns.countplot(x="CODE_GENDER", data=df_filtered, ax=ax8)
st.pyplot(fig8)

# 9. Countplot — Family Status
st.markdown("### 9. Family Status Distribution")
fig9, ax9 = plt.subplots(figsize=(8,4))
sns.countplot(y="NAME_FAMILY_STATUS", data=df_filtered, order=df_filtered["NAME_FAMILY_STATUS"].value_counts().index, ax=ax9)
st.pyplot(fig9)

# 10. Countplot — Education
st.markdown("### 10. Education Distribution")
fig10, ax10 = plt.subplots(figsize=(8,4))
sns.countplot(y="NAME_EDUCATION_TYPE", data=df_filtered, order=df_filtered["NAME_EDUCATION_TYPE"].value_counts().index, ax=ax10)
st.pyplot(fig10)


# Narrative Insights
st.markdown("## 📝 Narrative Insights")
st.markdown("""
- The portfolio has a **default rate of ~X%**, which is [higher/lower] than expected for retail lending.  
- Several features show **significant missingness (>40%)**, e.g., EXT_SOURCE_X — requiring imputation or exclusion.  
- **Income and credit distributions are right-skewed**, with extreme outliers (likely high-net-worth clients).  
- Age distribution suggests concentration in working-age borrowers (25–50).  
""")


