# AI-Powered Guest Experience Personalization System for Hospitality

## Project Overview
This project develops an AI-driven system to enhance hospitality guest experiences using Large Language Models (LLMs) like OpenAI GPT and Meta LLaMA. The system analyzes guest feedback, monitors sentiment trends, and dynamically personalizes recommendations for dining, activities, and amenities. By integrating real-time alerts for service teams, the solution ensures adaptive, tailored experiences that evolve with guest preferences during their stay.

## Key Outcomes
- **Personalized recommendations** for dining, activities, and amenities based on guest behavior analysis.
- **Real-time sentiment monitoring** to proactively address guest feedback.
- **Increased guest satisfaction** through dynamic personalization.
- **Automated alerts** for staff to resolve issues and optimize service delivery.

## Repository Structure & Milestones
The project is structured into four milestones, each building upon the previous one to develop a robust AI-powered guest experience system.

### **Milestone 1: Building & Evaluating a Machine Learning Model for Favorite Dish Prediction**
**Objective:** Predict the favorite dish of a customer based on their dining preferences and behavior.

#### **Key Steps:**
- **Data Preparation** – Loaded the dataset, split it into feature extraction, training, and testing sets based on time-based logic.
- **Feature Engineering** – Computed customer-level and cuisine-level features.
- **Data Integration** – Merged engineered features into the training and testing datasets.
- **Encoding & Model Training** – Applied one-hot encoding for categorical data and trained an XGBoost Classifier for dish prediction.
- **Model Evaluation** – Assessed model performance using accuracy, log loss, and feature importance analysis.

✅ **Outcome:** Developed an XGBoost model for predicting a guest’s favorite dish with 0.18 accuracy.

---

### **Milestone 2: Guest Preference Modeling & Personalized Recommendation System along with Booking UI**
**Objective:** Develop a recommendation engine to suggest personalized amenities and activities for guests.

#### **Key Steps:**
- Extracted features like frequency of activity participation, preferred times, and past spending patterns.
- Implemented **User-Based & Item-Based Filtering** to recommend relevant activities based on guest preferences.
- Used **TF-IDF & Cosine Similarity** to generate activity recommendations based on textual guest preferences.
- Combined **collaborative and content-based** approaches for improved accuracy.

✅ **Outcome:** Built a Hotel Booking UI with Personalized Recommendations that adapts to guest preferences and historical behaviors.

---

### **Milestone 3: Real-Time Sentiment Monitoring & Guest Feedback Analysis**
**Objective:** Analyze guest reviews using Natural Language Processing (NLP) to monitor sentiment trends and generate real-time alerts.

#### **Key Steps:**
- Loaded and cleaned guest feedback data, tokenized text, and removed stopwords.
- Created **Embeddings and inserted Metadata** into a vector database.
- Used **Sentiment Analysis** for rule-based sentiment scoring to gain deeper insights.
- Tracked sentiment over time and identified top positive/negative topics.
- Created **automated alerts** for hotel managers when negative sentiment was detected.

✅ **Outcome:** Implemented real-time guest sentiment tracking, allowing proactive issue resolution and improved guest satisfaction.

---

### **Milestone 4: Dashboard Development & Visualization**
**Objective:** Develop an interactive dashboard system for customer insights, sentiment analysis, and recommendations.

#### **Key Steps:**
- Created **interactive dashboards** for hotel bookings, dining insights, and customer review analysis.
- Used **Together.AI for graph-based visualization** of guest behavior patterns.
- Provided **real-time tracking** of service efficiency and guest satisfaction trends.
- Integrated all milestones into a seamless, user-friendly visualization interface.

✅ **Outcome:** Developed dashboards for **Hotel Bookings, Hotel Dining Insights, and Customer Review Analysis.**

---

## Installation & Setup
To run the system locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables (e.g., API keys for Together.AI, database credentials).
4. Run the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```
5. (Optional) Set up a MongoDB instance for database integration.

## Technologies Used
- **Machine Learning**: XGBoost, TF-IDF, Cosine Similarity
- **Natural Language Processing (NLP)**: OpenAI GPT, Meta LLaMA, Sentiment Analysis
- **Database & Storage**: MongoDB, Pinecone (Vector Storage)
- **Backend & API Integration**: Together.AI API, Flask
- **Visualization**: Streamlit, Matplotlib, Seaborn

## Future Enhancements
- **Improve Model Accuracy**: Experiment with deep learning techniques for better recommendation accuracy.
- **Enhance Sentiment Analysis**: Utilize transformer-based models like BERT for more nuanced sentiment analysis.
- **Expand Personalization Scope**: Extend recommendations beyond dining to include spa treatments, room preferences, and concierge services.
- **Multi-Language Support**: Implement multilingual NLP to cater to a diverse guest audience.

## Contributors
- **[Your Name]** – Project Lead
- **[Contributor 1]** – Machine Learning Engineer
- **[Contributor 2]** – Backend Developer
- **[Contributor 3]** – UI/UX Designer

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the OpenAI and Together.AI teams for providing API support and resources to enhance this project.

