# Milestone 3 - Hotel Review Analysis System

## Overview
Milestone 3 involved integrating Together AI embeddings, Pinecone for vector storage, and Streamlit for building an interactive UI. The project focused on processing hotel customer reviews, generating embeddings, storing them in a Pinecone index, retrieving relevant reviews, analyzing sentiments, and providing a manager-friendly review analysis dashboard.

## Customer Review Submission and Analysis
### Features:
- Customers submit hotel reviews in real-time.

### Sentiment Analysis:
- Used TextBlob to calculate sentiment score.
- If a negative review is submitted and the customer is currently staying, an automated email with room number, review, and sentiment score is sent to the hotel manager.

## Manager Review Analysis
### Built Using: 
- **Streamlit**

### Key Functionalities:
- **Query Input**: Allows managers to ask review-related questions.
- **Relevant Review Retrieval**: Uses Pinecone similarity search.
- **Summarization**: Together AI generates a professional summary of customer sentiments.
- **Word Cloud Generation**: Highlights frequently mentioned words based on the manager's query.
- **Data Download**: Managers can download the sentiment analysis report as a `.txt` file.

## Final Outcomes
⭐ Efficient storage and retrieval of customer reviews using Pinecone.

⭐ AI-powered summarization for quick managerial insights.

⭐ Real-time sentiment detection and manager notifications.

⭐ User-friendly Streamlit dashboard for customer and manager interactions.

⭐ Visualization enhancements using word clouds and sentiment scores.
## Customer Review Page
![Customer review UI](https://github.com/user-attachments/assets/b6f690a8-b4e6-42c9-8f8a-270aa98a6215)
![Customer UI](https://github.com/user-attachments/assets/6df3f40a-5ee6-47fd-9246-d4363e70650f)
![Analyse Customer UI](https://github.com/user-attachments/assets/cb69af33-2c74-4434-a89a-6dcc6d75ed6a)
## Manager Review Page
![Manager UI](https://github.com/user-attachments/assets/051ca477-c2f4-43b6-85f2-462fe688ef1e)
![Manager review page UI](https://github.com/user-attachments/assets/0cd38623-a737-40e1-88e4-d2a34547f201)

