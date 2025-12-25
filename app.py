import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="House Price Analysis", layout="wide")

# Path
base_path = r"C:\Users\kavi vala\Desktop\HOUSEPRICE"
data_path = os.path.join(base_path, "data", "housing_cleaned.csv")

# Load data
df = pd.read_csv(data_path)

st.title("🏠 House Price Data Analysis Dashboard")

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filter Options")

min_price, max_price = st.sidebar.slider(
    "Select Price Range",
    int(df.price.min()),
    int(df.price.max()),
    (int(df.price.min()), int(df.price.max()))
)

filtered_df = df[(df.price >= min_price) & (df.price <= max_price)]

# -------------------------
# KPI Section
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Average Price", f"{int(filtered_df.price.mean()):,}")
col2.metric("Average Area (sqft)", f"{int(filtered_df.area.mean())}")
col3.metric("Avg Price / Sqft", f"{int(filtered_df.price_per_sqft.mean())}")

# -------------------------
# Charts
# -------------------------

st.subheader("📊 Price Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df.price, bins=30, kde=True, ax=ax1)
st.pyplot(fig1)

st.subheader("📊 Area vs Price")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    x=filtered_df.area,
    y=filtered_df.price,
    ax=ax2
)
st.pyplot(fig2)

st.subheader("📊 Bedrooms vs Price")
fig3, ax3 = plt.subplots()
sns.boxplot(x=filtered_df.bedrooms, y=filtered_df.price, ax=ax3)
st.pyplot(fig3)

st.subheader("📊 Furnishing Status Impact")
fig4, ax4 = plt.subplots()
sns.barplot(
    x=filtered_df.furnishingstatus,
    y=filtered_df.price,
    ax=ax4
)
st.pyplot(fig4)

# -------------------------
# Insights Section
# -------------------------
st.subheader("🔍 Key Insights")

st.markdown("""
- Area aur price ke beech **strong positive relationship** hai  
- Furnished houses ka average price zyada hota hai  
- 3–4 bedroom houses **highest demand price range** me aate hain  
- Price per square feet ek important indicator hai locality value ka  
""")
