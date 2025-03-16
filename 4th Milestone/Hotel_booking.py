import streamlit as st
import pandas as pd
import pymongo
import plotly.express as px

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hotel_data"]
booking_collection = db["booking_data"]

# Fetch Data from MongoDB
def load_data():
    data = pd.DataFrame(list(booking_collection.find()))
    if "_id" in data.columns:
        data.drop(columns=["_id"], inplace=True)
    return data

# Load Data
data = load_data()

# Convert date columns
data["booking_date"] = pd.to_datetime(data["booking_date"], errors='coerce')

# Streamlit App
st.title("Hotel Booking Insights")

# Line Chart: Bookings Over Time
st.subheader("Bookings Trend Over Time")
fig = px.line(data, x="booking_date", y="booking_count", title="Daily Hotel Bookings")
st.plotly_chart(fig)

# Preferred Cuisine Analysis
st.subheader("Preferred Cuisine Analysis")
cuisine_count = data["preferred_cuisine"].value_counts()
st.bar_chart(cuisine_count)

# Average Length of Stay Analysis
st.subheader("Average Length of Stay")
data["stay_length"] = pd.to_numeric(data["stay_length"], errors='coerce')
avg_stay = data.groupby(pd.Grouper(key="booking_date", freq='M'))["stay_length"].mean()
fig = px.bar(avg_stay, title="Average Length of Stay (Monthly)")
st.plotly_chart(fig)
