# 🛍️ E-commerce Customer Churn Analysis & Prediction

This project analyzes customer behavior from a Brazilian e-commerce dataset (Olist) and predicts customer churn using RFM features and machine learning models.

---

## 📌 Objectives

- Understand customer purchasing behavior
- Define churn based on inactivity period
- Build RFM (Recency, Frequency, Monetary) features
- Train and evaluate churn prediction models

---

## 📊 Dataset

- Source: [Kaggle - Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Contains order, customer, product, seller, payment, and review information

---

## 🧪 RFM Feature Engineering

We engineered the following features for each customer:
- **Recency**: Days since last purchase
- **Frequency**: Total number of purchases
- **Monetary**: Total payment value

Churn was labeled if the customer had no purchases in the last 90 days of the dataset.

---

## 🤖 Models Used

Two models were trained:
- **Logistic Regression**: Baseline classification model
- **Random Forest**: More powerful ensemble model

---

## 🧠 Results

| Metric         | Logistic Regression | Random Forest |
|----------------|---------------------|----------------|
| Accuracy       | ✅ Good              | ✅✅ Great        |
| Precision/Recall | Balanced          | High recall (less false negatives) |

Feature importance analysis revealed **Recency** is the most predictive factor for churn.

---

## 📈 Visuals

- Feature importance bar chart
- Churn distribution plot
- RFM histograms (optional)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Scikit-learn
- Jupyter Notebook

---

## 💼 Key Takeaways

- RFM features are powerful predictors of churn
- Customers with high recency and low frequency are more likely to churn
- Churn prediction models help businesses focus on retention efforts

---

## 🚀 How to Run

1. Clone this repo
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
3. Run the notebook:  
   `notebooks/01_data_cleaning_and_eda.ipynb`
