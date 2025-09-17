## Memory optimiziation
import numpy as np
import pandas as pd
import streamlit as st
from utils.dataset import load_data 
from scipy.stats.mstats import winsorize

df=load_data()

def optimize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
  
    before = df.memory_usage(deep=True).sum() / 1024**2
    optimized = df.copy()

    for col in optimized.columns:
        s = optimized[col]

        # Integers type
        if pd.api.types.is_integer_dtype(s):
            vals = s.astype("int64")  # safe for bound checks
            if vals.min() >= np.iinfo(np.int8).min and vals.max() <= np.iinfo(np.int8).max:
                optimized[col] = s.astype("int8")
            elif vals.min() >= np.iinfo(np.int16).min and vals.max() <= np.iinfo(np.int16).max:
                optimized[col] = s.astype("int16")
            elif vals.min() >= np.iinfo(np.int32).min and vals.max() <= np.iinfo(np.int32).max:
                optimized[col] = s.astype("int32")

        # Floats type
        elif pd.api.types.is_float_dtype(s):
            s64 = s.astype("float64")
            if np.allclose(s64, s64.astype("float16"), rtol=1e-03, atol=1e-06, equal_nan=True):
                optimized[col] = s64.astype("float16")
            else:
                optimized[col] = s64.astype("float32")

    after = optimized.memory_usage(deep=True).sum() / 1024**2
    print(f"Memory: {before:.3f} MB → {after:.3f} MB ({(before - after) / before * 100:.2f}% reduction)")

    return optimized
optimized_df = optimize_dataframe(df)


## Feature Enginering(includes questions 1,2,3)

optimized_df['AGE_YEARS'] = optimized_df['DAYS_BIRTH'].apply(lambda x: x /-365.25 if x <= 0 else np.nan)
#convert Employment tenure
optimized_df['Employe worked'] = optimized_df['DAYS_EMPLOYED'].apply(lambda x: x /-365.25 if x <= 0 else np.nan)
#Create ratios:
optimized_df['DTI'] = optimized_df['AMT_ANNUITY'] / optimized_df['AMT_INCOME_TOTAL']
optimized_df['LOAN_TO_INCOME']= optimized_df['AMT_CREDIT'] / optimized_df['AMT_INCOME_TOTAL']
optimized_df['ANNUITY_TO_CREDIT'] = optimized_df['AMT_ANNUITY'] / optimized_df['AMT_CREDIT']

#Income Brackets 7th question
optimized_df["INCOME_BRACKET"] = pd.qcut(optimized_df["AMT_INCOME_TOTAL"],q=[0, 0.25,0.50, 0.75, 1.0],labels=["Low", "Mid-low","Mid-high","High"])

# Missing values treatment 4th queation
def treat_nulls(optimized_df: pd.DataFrame) -> pd.DataFrame:
   
    cleaned = optimized_df.copy()

    # 1. Drop columns with >60% nulls
    threshold = 0.6
    null_ratio = cleaned.isna().mean()
    to_drop = null_ratio[null_ratio > threshold].index
    cleaned = cleaned.drop(columns=to_drop)

    # 2. Handle remaining nulls
    for col in cleaned.columns:
        if cleaned[col].isna().any():
            if pd.api.types.is_numeric_dtype(cleaned[col]):
                median_val = cleaned[col].median()
                cleaned[col] = cleaned[col].fillna(median_val)

            elif pd.api.types.is_datetime64_any_dtype(cleaned[col]):
                cleaned[col] = cleaned[col].fillna(method="ffill").fillna(method="bfill")

            else:
                mode_val = cleaned[col].mode(dropna=True)
                if not mode_val.empty:
                    cleaned[col] = cleaned[col].fillna(mode_val[0])
                else:
                    cleaned[col] = cleaned[col].fillna("")

    return cleaned
cleaned_df= treat_nulls(optimized_df)

def preprocess_dataframe(df: pd.DataFrame, categorical_cols=None, numeric_cols=None, cat_threshold=0.01, win_limits=(0.01, 0.01)) -> pd.DataFrame:
    processed = df.copy()  

    # 1. Standardize rare categories 5th question
    def merge_rare(series, threshold=0.01):
        repeat = series.value_counts(normalize=True)
        end = repeat[repeat < threshold].index
        return series.replace(end, "Other")

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = merge_rare(df[col])

    # 2. Winsorize numeric features 6th question
    def winsorize(s):
        return np.clip(s, s.quantile(0.01), s.quantile(0.99))

    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = winsorize(df[col])


    return processed
final_df = preprocess_dataframe(cleaned_df)

final_df["CODE_GENDER"] = final_df["CODE_GENDER"].replace({"XNA": "Other"})
final_df["NAME_EDUCATION_TYPE"] = final_df["NAME_EDUCATION_TYPE"].replace({"Academic degree": "Higher education"})
final_df["NAME_FAMILY_STATUS"] = final_df["NAME_FAMILY_STATUS"].replace({"Unknown": "Other"})
final_df["NAME_HOUSING_TYPE"] = final_df["NAME_HOUSING_TYPE"].replace({"Co-op apartment": "Other"})


# Global filter function
def Global_filters(df):
    gender = st.sidebar.multiselect("Gender", df["CODE_GENDER"].unique())
    education = st.sidebar.multiselect("Education", df["NAME_EDUCATION_TYPE"].unique())
    family = st.sidebar.multiselect("Family Status", df["NAME_FAMILY_STATUS"].unique())
    housing = st.sidebar.multiselect("Housing", df["NAME_HOUSING_TYPE"].unique())
    age_range = st.sidebar.slider("Age Range", 18, 70, (20, 60))
    income_range = st.sidebar.slider("Income Range", int(df["AMT_INCOME_TOTAL"].min()), 
                                     int(df["AMT_INCOME_TOTAL"].max()), 
                                     (50000, 500000))

    df_filtered = df[
        (df["CODE_GENDER"].isin(gender) if gender else True) &
        (df["NAME_EDUCATION_TYPE"].isin(education) if education else True) &
        (df["NAME_FAMILY_STATUS"].isin(family) if family else True) &
        (df["NAME_HOUSING_TYPE"].isin(housing) if housing else True) &
        (df["AGE_YEARS"].between(*age_range)) &
        (df["AMT_INCOME_TOTAL"].between(*income_range))
    ]
    return df_filtered
#     
