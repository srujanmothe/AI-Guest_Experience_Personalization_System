import streamlit as st
import pandas as pd
import pymongo
import plotly.express as px

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hotel_data"]
dining_collection = db["dining_data"]

# Fetch Data from MongoDB
def load_data():
    data = pd.DataFrame(list(dining_collection.find()))
    if "_id" in data.columns:
        data.drop(columns=["_id"], inplace=True)
    return data

# Load Data
data = load_data()

# Convert date columns
data["dining_date"] = pd.to_datetime(data["dining_date"], errors='coerce')

# Streamlit App
st.title("Dining Insights")

# Pie Chart: Average Dining Cost by Cuisine
st.subheader("Average Dining Cost by Cuisine")
dining_avg_cost = data.groupby("cuisine")["cost"].mean().reset_index()
fig = px.pie(dining_avg_cost, names="cuisine", values="cost", title="Cost Distribution by Cuisine")
st.plotly_chart(fig)

# Customer Count Over Time
st.subheader("Customer Count Over Time")
cust_count = data.groupby("dining_date")["customer_count"].sum().reset_index()
fig = px.line(cust_count, x="dining_date", y="customer_count", title="Customer Count Over Time")
st.plotly_chart(fig)
