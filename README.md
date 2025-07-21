# 📦 E-commerce Product Delivery Prediction

This project predicts whether an e-commerce product will reach the customer **on time or be delayed**.  
The goal is to help an international electronics e-commerce company **optimize its logistics**, **improve customer satisfaction**, and **gain insights** into factors affecting delivery performance.

--------------------------------

## ◈ Project Overview

- **Domain:** E-commerce Logistics
- **Task:** Binary classification — On Time (`1`) or Late (`0`) delivery
- **Technique:** Machine Learning pipeline with preprocessing, model selection, hyperparameter tuning, and evaluation.
- **Tools:** Python, pandas, scikit-learn, seaborn, matplotlib, Jupyter Notebook

-------------------------------

## ◈ Problem Statement

Timely delivery is a key factor in e-commerce customer satisfaction.  
Delays can damage brand reputation, increase costs, and lower repeat purchases.

**Objective:** Build a robust machine learning model that can predict if an order will be delivered on time based on features such as:
- Product weight, cost, discount
- Warehouse block, mode of shipment
- Customer rating, prior purchases, etc.

--------------------------

## Dataset

- Source: E-commerce shipping dataset (CSV)
- Rows: ~11,000 orders
- Features:
  - **Numerical:** Cost of Product, Discount Offered, Weight, Customer Rating, Prior Purchases
  - **Categorical:** Warehouse Block, Mode of Shipment, Product Importance, Gender
  - **Target:** `Reached.on.Time_Y.N` — (1: On Time, 0: Late)

---

## ◈ Exploratory Data Analysis (EDA)

- Checked for missing values & duplicates
- Visualized numerical feature distributions (histograms, KDE plots)
- Analyzed categorical features (countplots)
- Checked correlation matrix
- Identified outliers using boxplots

---

## ◈ Feature Engineering

- Dropped irrelevant columns: `ID`, `Gender` (low signal)
- One-hot encoded categorical features (`Warehouse_block`, `Mode_of_Shipment`)
- Scaled numerical features with `StandardScaler`
- Checked for multicollinearity (VIF)

---

##  Model Building & Selection

- Split data: 80% train, 20% test
- Pipelines with `ColumnTransformer` for consistent preprocessing
- Trained 4 baseline models:
  - Random Forest
  - Logistic Regression
  - Decision Tree
  - K-Nearest Neighbors (KNN)
- Evaluated using accuracy and classification report

---

##  Hyperparameter Tuning

- Identified the **best model** based on test accuracy (Random Forest).
- Tuned the best model using `GridSearchCV`:
  - Parameters tuned: number of trees, max depth, min samples per leaf/split
- Evaluated best model:
  - Confusion Matrix
  - Accuracy, Precision, Recall, F1-Score
  - Focused on reducing false negatives (missed late deliveries)

---

## ◈ Final Results

- **Best Model:** Random Forest Classifier
- **Test Accuracy:** ~69%
- **Key Insight:** Discount Offered, Cost of Product, and Mode of Shipment were significant predictors.

---

##  Project Deliverables

- Jupyter Notebook (`Ecommerce-product.ipynb`) — with code, EDA, and model steps.
  Visualizations — distribution plots, correlation heatmaps, confusion matrices.
- Saved trained pipeline: `final_delivery_model.pkl` (ready for production use)
- Streamlit-ready script for live predictions (optional)

---

✦ Power Bi Dashboard:
-------------------

<img width="2000" height="1104" alt="image" src="https://github.com/user-attachments/assets/13ba5926-661a-47ff-935a-2acade63f384" />


✦ Streamlit App:
-------------------
<img width="1913" height="928" alt="image" src="https://github.com/user-attachments/assets/d42aec1b-34ee-4962-8792-ef2f7aae95b5" />



## ◈ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/ecommerce-delivery-prediction.git
   cd ecommerce-delivery-prediction
