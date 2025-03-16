# AI-Powered Guest Experience Personalization System for Hospitality

## Project Overview
This project focuses on enhancing guest experiences in the hospitality industry using AI-driven personalization. By leveraging Large Language Models (LLMs) such as OpenAI GPT and Meta LLaMA, the system analyzes guest feedback, monitors sentiment trends, and provides personalized recommendations for dining, activities, and amenities. Additionally, real-time alerts help service teams proactively address guest concerns and optimize service delivery.

## Key Features
- **Personalized Recommendations**: AI-driven suggestions for dining, activities, and amenities based on guest behavior.
- **Sentiment Monitoring**: Real-time tracking of guest feedback for proactive service improvements.
- **Automated Staff Alerts**: Instant notifications for staff to address guest concerns.
- **Interactive Dashboards**: Visual insights into hotel bookings, customer preferences, and review sentiments.

## Repository Structure
The project is divided into four milestones, each contributing to the development of the guest experience system.

### **Milestone 1: Predicting Favorite Dish using Machine Learning**
- **Objective**: Develop an XGBoost-based model to predict a guest’s favorite dish.
- **Steps**:
  - Prepared the dataset and split it into training and testing sets.
  - Engineered features at the customer and cuisine levels.
  - Applied one-hot encoding and trained an XGBoost Classifier.
  - Evaluated model performance using accuracy and log loss.
- **Outcome**: Achieved a baseline accuracy of 18% for dish predictions.

### **Milestone 2: Personalized Recommendations & Hotel Booking UI**
- **Objective**: Implement a booking system with personalized recommendations.
- **Steps**:
  - Extracted user behavior insights and created preference-based features.
  - Implemented collaborative and content-based recommendation models.
  - Developed a user-friendly hotel booking interface with dynamic recommendations.
- **Outcome**: A fully functional booking UI with personalized dining and activity suggestions.

### **Milestone 3: Sentiment Analysis & Real-Time Monitoring**
- **Objective**: Analyze customer reviews to track sentiment and generate alerts.
- **Steps**:
  - Processed and embedded guest feedback for sentiment analysis.
  - Used NLP-based sentiment scoring to classify reviews.
  - Created an automated alert system for negative feedback.
- **Outcome**: Real-time sentiment monitoring and proactive service adjustments.

### **Milestone 4: Interactive Dashboard & Data Visualization**
- **Objective**: Develop dashboards for insights into guest behaviors and hotel operations.
- **Steps**:
  - Built dashboards for hotel bookings, dining insights, and customer review analysis.
  - Integrated AI-generated insights for data interpretation.
  - Provided real-time tracking of guest satisfaction trends.
- **Outcome**: Intuitive dashboards for hotel management and guest engagement.

## Technologies Used
- **Machine Learning**: XGBoost, TF-IDF, Cosine Similarity
- **Natural Language Processing**: OpenAI GPT, Meta LLaMA, Sentiment Analysis
- **Database & Storage**: MongoDB, Pinecone for vector storage
- **Web Frameworks**: Streamlit for UI development
- **Automation & Alerts**: SMTP for email notifications, Together.AI for AI-generated insights

## Future Enhancements
- **Improved Recommendation Algorithms**: Experiment with deep learning techniques.
- **Enhanced Sentiment Analysis**: Implement transformer-based models for review analysis.
- **Expanded Personalization Features**: Incorporate additional guest data for deeper insights.
- **Mobile Application Integration**: Extend functionalities for seamless access.

This project delivers an AI-powered solution that transforms guest experiences, providing hotels with the tools needed for personalized service, real-time feedback tracking, and data-driven decision-making.
