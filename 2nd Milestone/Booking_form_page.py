import streamlit as st
import pandas as pd
import os
from langchain_together import TogetherEmbeddings
from pinecone import Pinecone
from together import Together
import datetime

# 🔹 Set API Keys
os.environ["TOGETHER_API_KEY"] = "d0138d7876bde3db01c9b87dd4a7fc88b67d130c13d26cb8db4b874cd6feb275"

# 🔹 Initialize Pinecone & Together AI
pc = Pinecone(api_key="pcsk_3Akygq_37NwsGLrrUn2yjAhpNymMFUxqh5ggkET7tZHnmfiuyiwvCFWu5a3gRD3mCvp1KX")
embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval")
index = pc.Index(host="hotel-reviews-t1jsbtd.svc.aped-4627-b74a.pinecone.io")
client = Together()

# 🔹 Load Existing Reviews from Excel
data_file = "reviews_data.xlsx"
numeric_data_file = "review_data_numeric.xlsx"
if os.path.exists(data_file):
    reviews_df = pd.read_excel(data_file).dropna(how='all')
else:
    reviews_df = pd.DataFrame(columns=["review_id", "customer_id", "Review", "review_date", "Rating"])

if os.path.exists(numeric_data_file):
    numeric_reviews_df = pd.read_excel(numeric_data_file).dropna(how='all')
else:
    numeric_reviews_df = pd.DataFrame(columns=["review_id", "customer_id", "Rating"])

# 🔹 Streamlit UI
st.title("🍽️ Customer Review Page")
st.write("Submit your review and analyze customer sentiment !!  It's helps us improve. 💬")

# 🔹 User Inputs for Review Submission
st.subheader("✍️ Write Your Review")
customer_id = st.text_input("🔢 Customer ID", placeholder="Enter your Customer ID")
review_text = st.text_area("Write your review here:", placeholder="Share your experience...")
review_date = st.date_input("📅 Review Date", value=datetime.date.today())
rating = st.slider("⭐ Rate your experience (1 = Poor, 10 = Excellent)", 1, 10, 5)

# 🔹 Submit Review Button
if st.button("Submit Review"):
    if review_text.strip() == "" or customer_id.strip() == "":
        st.error("❌ Please enter both Customer ID and review before submitting.")
    else:
        # Generate a unique Review ID
        review_id = f"R{len(reviews_df) + 1:05d}"
        
        # Generate embedding for the review
        review_embedding = embeddings.embed_query(review_text)
        
        # Store the review in Pinecone
        index.upsert(vectors=[{
            "id": review_id,
            "values": review_embedding,
            "metadata": {
                "customer_id": customer_id,
                "Review": review_text,
                "review_date": review_date.strftime("%Y-%m-%d"),
                "Rating": rating
            }
        }])
        
        # Append new review to DataFrame
        new_review = pd.DataFrame({
            "review_id": [review_id],
            "customer_id": [customer_id],
            "Review": [review_text],
            "review_date": [review_date.strftime("%Y-%m-%d")],
            "Rating": [rating]
        })
        reviews_df = pd.concat([reviews_df, new_review], ignore_index=True).dropna(how='all')
        
        # Append to numeric dataset
        new_numeric_review = pd.DataFrame({
            "review_id": [review_id],
            "customer_id": [customer_id],
            "Rating": [rating]
        })
        numeric_reviews_df = pd.concat([numeric_reviews_df, new_numeric_review], ignore_index=True).dropna(how='all')
        
        # Save to Excel
        reviews_df.to_excel(data_file, index=False)
        numeric_reviews_df.to_excel(numeric_data_file, index=False)
        st.success("✅ Thank you for your review! It has been saved and stored in Pinecone.")
        
        # Show submitted reviews
        st.session_state.show_reviews = True

# 🔹 Display Submitted Reviews (Initially Hidden)
if "show_reviews" not in st.session_state:
    st.session_state.show_reviews = False

if st.session_state.show_reviews:
    if not reviews_df.empty:
        st.subheader("📋 Submitted Reviews")
        st.dataframe(reviews_df[["review_id", "customer_id", "Review", "review_date", "Rating"]])

# 🔹 Sentiment Analysis Section
st.subheader("🔍 Analyze Customer Sentiment")
query = st.text_input("Enter a query about customer reviews:", "How is the food quality?")
rating_filter = st.slider("⭐ Filter Reviews by Rating", 1, 10, (1, 10))

if st.button("Analyze Sentiment"):
    if query:
        # Generate embedding for the query
        query_embedding = embeddings.embed_query(query)
        
        # 🔎 Search in Pinecone
        results = index.query(vector=query_embedding, top_k=5, include_metadata=True)
        
        # 🔄 Include the latest review as well
        latest_review = reviews_df.iloc[-1].to_dict() if not reviews_df.empty else None
        if latest_review:
            results["matches"].insert(0, {"metadata": latest_review})
        
        # 🔄 Filter results based on user-selected rating
        filtered_reviews = []
        for match in results['matches']:
            metadata = match['metadata']
            review_rating = metadata.get("Rating", 5)
            
            # Apply rating filter
            if rating_filter[0] <= review_rating <= rating_filter[1]:
                filtered_reviews.append(metadata)

        # 📋 Display Results
        if filtered_reviews:
            st.subheader("📊 Matching Reviews")
            st.write(pd.DataFrame(filtered_reviews)[["review_id", "customer_id", "Review", "review_date", "Rating"]])
        else:
            st.warning("⚠️ No matching reviews found for the given filters.")
    else:
        st.error("❌ Please enter a query to analyze sentiment.")
