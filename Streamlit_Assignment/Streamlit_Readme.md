# 📊 Portfolio Risk Dashboard

A **Streamlit-based interactive dashboard** to explore and monitor loan applications, borrower characteristics, and repayment outcomes.  
This dashboard provides a **360° view of portfolio health**, highlights potential risks, and supports **data-driven decision-making**.

---

## 🚀 Features

- **Global Filters**  
  Filter data by gender, education, housing, family status, income, and age.  

- **Multi-Page Navigation**  
  - 🏠 **Home** → Introduction, usage guide, and goals.  
  - 📊 **Overview & Data Quality** → Dataset summary, missing values, and KPIs.  
  - 👨‍👩‍👧 **Demographics & Household** → Borrower profiles (age, family, children).  
  - 💳 **Credit & Loan Behavior** → Loan size, income, credit ratios.  
  - 📈 **Risk Segmentation** → Compare defaulters vs. non-defaulters.  

- **Preprocessing Pipeline**  
  - Memory optimization  
  - Missing value treatment  
  - Feature engineering (Age, DTI, Loan-to-Income, etc.)  
  - Handling rare categories & winsorization  

---

## 📂 Project Structure
├── home.py # Streamlit Home Page (intro, usage, goals)
├── preprocessing.py # Data preprocessing & global filters
├── utils/
│ └── dataset.py # Custom load_data function (loads from Drive link)
├── pages/
│ ├── 1_Overview.py # Dataset quality & KPIs
│ ├── 2_Credit.py # Credit & loan analysis
│ ├── 3_Demographics.py # Demographics & household profile
│ ├── 4_Risk.py # Risk segmentation
├── practice.ipynb # Practice notebook for testing analysis
└── README.md # Project documentation
📊 Dataset

The dataset is not uploaded directly due to size.

Instead, it is loaded from a Google Drive link using the custom load_data() function inside utils/dataset.py.

Update the Drive link inside load_data() if you want to replace with your own dataset.

🎯 Main Goals

Detect default patterns.

Identify high-risk borrower groups.

Evaluate data quality issues.

Support credit policy and decision-making.

💡 What You Will Learn

By interacting with this dashboard, you will discover:

📊 Portfolio Health → Borrower counts & default rate.

👨‍👩‍👧 Borrower Profiles → Risk distribution by demographics.

💳 Credit Behavior → Risk linked to income & loan sizes.

⚠️ Early Risk Indicators → Insights to guide financial decisions.

🛠 Requirements

Python 3.8+

Streamlit

Pandas, NumPy, Matplotlib, SciPy

Install via:

pip install streamlit pandas numpy matplotlib scipy

📌 Notes

Replace the Google Drive link in utils/dataset.py with your own if the original is inaccessible.

Ensure that the Drive file is shared with "Anyone with the link" for proper loading.