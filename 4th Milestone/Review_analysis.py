import streamlit as st
import pandas as pd
import pymongo
import plotly.express as px
from textblob import TextBlob

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hotel_data"]
reviews_collection = db["reviews_data"]

# Fetch Data from MongoDB
def load_data():
    data = pd.DataFrame(list(reviews_collection.find()))
    if "_id" in data.columns:
        data.drop(columns=["_id"], inplace=True)
    return data

# Load Data
data = load_data()

# Sentiment Analysis
def analyze_sentiment(text):
    if pd.isna(text):
        return "Neutral"
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

data["sentiment"] = data["review_text"].apply(analyze_sentiment)

# Streamlit App
st.title("Hotel Reviews Analysis")

# Sentiment Pie Chart
st.subheader("Sentiment Distribution")
sentiment_counts = data["sentiment"].value_counts().reset_index()
fig = px.pie(sentiment_counts, names="index", values="sentiment", title="Sentiment Analysis of Reviews")
st.plotly_chart(fig)

# Rating Distribution Histogram
st.subheader("Rating Distribution")
fig = px.histogram(data, x="rating", title="Distribution of Review Ratings")
st.plotly_chart(fig)
