import streamlit as st
import pandas as pd
import joblib
import time
import base64
import warnings
import sys

# DEBUGGING SECTION - START
st.write("🔍 **Debug Information:**")

# Python version check
st.write(f"Python version: {sys.version}")

# Numpy debugging
try:
    import numpy as np
    st.success(f"✅ Numpy successfully imported - Version: {np.__version__}")
    st.write(f"Numpy location: {np.__file__}")
except ImportError as e:
    st.error(f"❌ Numpy import error: {e}")

# Pandas debugging
try:
    import pandas as pd
    st.success(f"✅ Pandas successfully imported - Version: {pd.__version__}")
except ImportError as e:
    st.error(f"❌ Pandas import error: {e}")

# Scikit-learn debugging
try:
    import sklearn
    st.success(f"✅ Scikit-learn successfully imported - Version: {sklearn.__version__}")
except ImportError as e:
    st.error(f"❌ Scikit-learn import error: {e}")

# Joblib debugging
try:
    import joblib
    st.success(f"✅ Joblib successfully imported - Version: {joblib.__version__}")
except ImportError as e:
    st.error(f"❌ Joblib import error: {e}")

# Imbalanced-learn debugging
try:
    import imblearn
    st.success(f"✅ Imbalanced-learn successfully imported - Version: {imblearn.__version__}")
except ImportError as e:
    st.error(f"❌ Imbalanced-learn import error: {e}")

st.write("---")
# DEBUGGING SECTION - END


model = joblib.load('final_delivery_model.joblib')

st.set_page_config(
    page_title="E-commerce Order Tracker",
    layout="centered",
    page_icon="🚚"
)

# ✅ Custom CSS: full purple sidebar, custom sliders, dropdowns, file uploader, button
st.markdown("""
<style>
/* Page */
.stApp {
  background-color: #f9f5ff;
 
}

/* Header */
.header-container {
    width: 100%; 
    background-color:#9C27B0; padding: 8px 0;
    text-align: center; 
    position: fixed; 
    top: 0; 
    left: 0;
    margin-left: 0rem;         /* move it to the right */
    color: white; 
    z-index: 999; 
    right: 0;
    height: 80px;  /* increase this */
}
.header-container h2 {
    color: white; 
    font-size: 1.5em;
    font-family: Arial, sans-serif;
    text-align: center; 
    margin: 0;
}
             @keyframes scroll-left {
        0% {
            transform: translateX(100%);
        }
        100% {
            transform: translateX(-100%);
        }
    }
    @keyframes scroll-left {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-100%); }
}
            @media (max-width: 768px) {
  .stApp {
    padding-top: 220px !important;
  }
}
            

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #320132;  /* Deep purple */
    color: white;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p {
    color: white;
             
}

/* Sliders */           
/* Slider parent container */
div[data-baseweb="slider"] > div {
  color: #fff !important;
  background: #4d004d !important;
  border-radius: 2px !important;
  height: 24px !important;
  width: 102%;
}

/* Slider value bubble */
div[data-baseweb="slider"] span {
  background-color: #0d001a !important;
  color: white !important;
  border-radius: 4px !important;
  padding: 2px 6px !important;
}

/* Slider track */
span[data-baseweb="slider-track"] {
  border-radius: 5px !important;
  height: 14px !important;
  background: linear-gradient(90deg, #9C27B0, #E040FB) !important;
}

/* Slider handle (thumb) */
span[data-baseweb="slider-thumb"] {
  border: 2px solid #000000 !important;
  background: #FF5722 !important;
  width: 20px !important;
  height: 20px !important;
}

/* Dropdown */
div[data-baseweb="select"] {
  background-color: #320132 !important;
  border-radius: 4px !important;
  color: white !important;
  border: 2px solid #000000 !important;
            
}

/* The text inside the selectbox */
div[data-baseweb="select"] * {
  color: white !important;
background-color: #320132 !important;
            
}

/* File uploader */
/* File uploader box styling */
section[data-testid="stFileUploaderDropzone"] {
  background-color: #320132 !important;
  border: 2px solid #000000 !important;
  border-radius: 8px !important;
  color: white !important;
}

/* File uploader text */
section[data-testid="stFileUploaderDropzone"] * {
  color: white !important;
    background-color: #4d004d !important;
}
            
/* Predict button */
div.stButton > button {
    background-color: #4d004d;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5em 2em;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #1a0033;
            color:white;
}

/* Footer */
footer {
    position: fixed; 
    bottom: 0; left: 0; 
    height: 60px; width: 100%;
    background-color: black; 
    color: white; 
    text-align: center;
    padding: 10px; 
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)


# Read and encode your local image
with open("images/return.png", "rb") as f:
    data = f.read()
encoded = base64.b64encode(data).decode()

# ✅ Header
st.markdown(f"""
<div class="header-container">
    <div style="
    width: 100%;
    background-color: #9C27B0;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
            ">
    <img src="data:image/jpg;base64,{encoded}" alt="Logo" height="60px" width="70px" style="border-radius: 50%;margin-left: 180px;">
            <h2 style="color: white;text-shadow: 2px 2px 5px #000, -2px -2px 5px #000;"> E-Commerce Product Delivery Status Tracker! </h2></div>
</div>
""", unsafe_allow_html=True)


# ✅ Marquee
st.markdown("""
<marquee behavior="scroll" direction="left" scrollamount="10"
style="color: #7B1FA2; font-weight: bold; font-size: 1.2rem;">
📢 Stay updated! Your order is in safe hands and on its way to your doorstep. Thank you for shopping with us! 🛍️✨
</marquee>
""", unsafe_allow_html=True)

# ✅ Sidebar inputs
st.sidebar.header("📦 Enter Order Details")
Customer_care_calls = st.sidebar.slider("Customer Care Calls", 0, 10, 2)
Customer_rating = st.sidebar.slider("Customer Rating", 1, 5, 3)
Cost_of_the_Product = st.sidebar.slider("Cost of the Product", 50, 500, 200)
Discount_offered = st.sidebar.slider("Discount Offered (%)", 0, 65, 10)
Weight_in_gms = st.sidebar.slider("Weight (grams)", 100, 5000, 1500)
Prior_purchases = st.sidebar.slider("Prior Purchases", 0, 20, 5)

Warehouse_block = st.sidebar.selectbox("Warehouse Block", ["A", "B", "C", "D", "F"])
Mode_of_Shipment = st.sidebar.selectbox("Mode of Shipment", ["Ship", "Flight", "Road"])
Product_importance = st.sidebar.selectbox("Product Importance", ["low", "medium", "high"])
uploaded_file = st.sidebar.file_uploader("Upload Shipment Label (optional)",
                                         type=['xlsx', 'xls', 'png', 'jpg', 'jpeg'])

# ✅ Main input summary
input_df = pd.DataFrame([{
    'Customer_care_calls': Customer_care_calls,
    'Customer_rating': Customer_rating,
    'Cost_of_the_Product': Cost_of_the_Product,
    'Discount_offered': Discount_offered,
    'Weight_in_gms': Weight_in_gms,
    'Prior_purchases': Prior_purchases,
    'Warehouse_block': Warehouse_block,
    'Mode_of_Shipment': Mode_of_Shipment,
    'Product_importance': Product_importance
}])

st.subheader("📜 Order Summary")
st.dataframe(input_df)

# ✅ Predict
if st.button("Predict"):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    if uploaded_file and uploaded_file.name.endswith(('.xlsx', '.xls')):
        df_excel = pd.read_excel(uploaded_file)
        predictions = model.predict(df_excel)
        df_excel["Delivery Status"] = ["On Time" if p == 0 else "Delayed" for p in predictions]

        st.success("✅ Predictions added for uploaded file!")
        st.dataframe(df_excel)

        csv = df_excel.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="predicted_orders.csv",
            mime='text/csv'
        )
    else:
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.error("❌ Oops! This delivery is likely to be **Delayed**")
            st.image("delay.jpg", caption="Predicted: Delayed" )

        else:
            st.success("✅ Great news! Your delivery is predicted to be **On Time**")
            st.image("delivery1.jpg", caption="Predicted: On Time")
            st.balloons()

# ✅ Footer
st.markdown('<footer>© 2025 E-commerce Delivery Tracker | Capstone Project<br> Built with ❤️ using Streamlit</footer>',
            unsafe_allow_html=True)
