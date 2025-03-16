import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Sample Data Generation
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    cuisines = ["South Indian", "North Indian", "Multi"]
    reviews = ["Positive", "Neutral", "Negative"]
    data = {
        "date": dates,
        "bookings": np.random.randint(50, 200, size=len(dates)),
        "cuisine": np.random.choice(cuisines, size=len(dates)),
        "stay_duration": np.random.randint(1, 10, size=len(dates)),
        "review": np.random.choice(reviews, size=len(dates)),
        "rating": np.random.randint(1, 6, size=len(dates)),
        "dining_cost": np.random.randint(100, 1000, size=len(dates)),
    }
    return pd.DataFrame(data)

# Load sample data
df = generate_sample_data()

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the dashboard with tabs
app.layout = html.Div([
    html.H1("Hotel Management Dashboard", style={"textAlign": "center"}),
    
    # Tabs for different dashboards
    dcc.Tabs(id="tabs", value="tab-1", children=[
        dcc.Tab(label="Hotel Booking Insights", value="tab-1"),
        dcc.Tab(label="Dining Insights", value="tab-2"),
        dcc.Tab(label="Reviews Analysis", value="tab-3"),
    ]),
    
    # Tab content
    html.Div(id="tabs-content")
])

# Callbacks to render tab content
@app.callback(
    Output("tabs-content", "children"),
    Input("tabs", "value")
)
def render_tab_content(tab):
    if tab == "tab-1":
        # Hotel Booking Insights
        return html.Div([
            html.H2("Hotel Booking Insights"),
            
            # Bookings per Day (Scatter Plot)
            html.Div([
                html.H3("Bookings per Day"),
                dcc.Graph(id="bookings-per-day", figure=px.scatter(df, x="date", y="bookings", title="Bookings per Day"))
            ]),
            
            # Trend of Cuisines Over Time (Bar Plot)
            html.Div([
                html.H3("Trend of Cuisines Over Time"),
                dcc.Graph(id="cuisine-trend", figure=px.bar(df.groupby(["date", "cuisine"]).size().reset_index(name="count"), 
                                                           x="date", y="count", color="cuisine", title="Trend of Cuisines Over Time"))
            ]),
            
            # Average Stay Duration per Customer (Weekly Scatter Plot)
            html.Div([
                html.H3("Average Stay Duration per Customer (Weekly)"),
                dcc.Graph(id="stay-duration-weekly", figure=px.scatter(df.resample("W", on="date").mean().reset_index(), 
                                                                      x="date", y="stay_duration", title="Average Stay Duration per Customer (Weekly)"))
            ]),
        ])
    
    elif tab == "tab-2":
        # Dining Insights
        return html.Div([
            html.H2("Dining Insights"),
            
            # Average Dining Cost by Cuisine (Pie Chart)
            html.Div([
                html.H3("Average Dining Cost by Cuisine"),
                dcc.Graph(id="dining-cost-pie", figure=px.pie(df.groupby("cuisine")["dining_cost"].mean().reset_index(), 
                                                             names="cuisine", values="dining_cost", title="Average Dining Cost by Cuisine"))
            ]),
            
            # Customer Count Over Time (Line Chart)
            html.Div([
                html.H3("Customer Count Over Time"),
                dcc.Graph(id="customer-count-line", figure=px.line(df.groupby("date").size().reset_index(name="count"), 
                                                                  x="date", y="count", title="Customer Count Over Time"))
            ]),
        ])
    
    elif tab == "tab-3":
        # Reviews Analysis
        return html.Div([
            html.H2("Reviews Analysis"),
            
            # Sentiment Analysis (Pie Chart)
            html.Div([
                html.H3("Sentiment Analysis"),
                dcc.Graph(id="sentiment-pie", figure=px.pie(df["review"].value_counts().reset_index(), 
                                                           names="index", values="review", title="Sentiment Analysis"))
            ]),
            
            # Rating Distribution (Histogram)
            html.Div([
                html.H3("Rating Distribution"),
                dcc.Graph(id="rating-histogram", figure=px.histogram(df, x="rating", title="Rating Distribution"))
            ]),
        ])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)