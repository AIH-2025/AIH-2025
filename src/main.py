import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="AIH-2025 Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🚀 AIH-2025")
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Dashboard", "Data Visualization", "Interactive Tools", "About"]
)

# Sample data generation
@st.cache_data
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'date': dates,
        'sales': np.random.normal(1000, 200, len(dates)),
        'users': np.random.normal(500, 100, len(dates)),
        'revenue': np.random.normal(5000, 1000, len(dates)),
        'category': np.random.choice(['A', 'B', 'C'], len(dates))
    }
    return pd.DataFrame(data)

# Generate data
df = generate_sample_data()

if page == "Dashboard":
    st.markdown('<h1 class="main-header">📊 AIH-2025 Dashboard</h1>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Sales</h3>
            <h2>${:,.0f}</h2>
        </div>
        """.format(df['sales'].sum()), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Users</h3>
            <h2>{:,.0f}</h2>
        </div>
        """.format(df['users'].sum()), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Revenue</h3>
            <h2>${:,.0f}</h2>
        </div>
        """.format(df['revenue'].sum()), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Avg Daily Sales</h3>
            <h2>${:,.0f}</h2>
        </div>
        """.format(df['sales'].mean()), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Sales Trend")
        fig_sales = px.line(df, x='date', y='sales', title='Daily Sales')
        fig_sales.update_layout(height=400)
        st.plotly_chart(fig_sales, use_container_width=True)
    
    with col2:
        st.subheader("👥 Users Trend")
        fig_users = px.line(df, x='date', y='users', title='Daily Users')
        fig_users.update_layout(height=400)
        st.plotly_chart(fig_users, use_container_width=True)
    
    # Revenue chart
    st.subheader("💰 Revenue Analysis")
    fig_revenue = px.bar(df.groupby('category')['revenue'].sum().reset_index(), 
                        x='category', y='revenue', title='Revenue by Category')
    st.plotly_chart(fig_revenue, use_container_width=True)

elif page == "Data Visualization":
    st.markdown('<h1 class="main-header">📊 Data Visualization</h1>', unsafe_allow_html=True)
    
    # Data filters
    st.subheader("🔍 Data Filters")
    col1, col2 = st.columns(2)
    
    with col1:
        date_range = st.date_input(
            "Select Date Range",
            value=(df['date'].min().date(), df['date'].max().date()),
            min_value=df['date'].min().date(),
            max_value=df['date'].max().date()
        )
    
    with col2:
        selected_categories = st.multiselect(
            "Select Categories",
            options=df['category'].unique(),
            default=df['category'].unique()
        )
    
    # Filter data
    if len(date_range) == 2:
        filtered_df = df[
            (df['date'].dt.date >= date_range[0]) &
            (df['date'].dt.date <= date_range[1]) &
            (df['category'].isin(selected_categories))
        ]
    else:
        filtered_df = df[df['category'].isin(selected_categories)]
    
    # Visualization options
    st.subheader("📊 Visualization Options")
    viz_type = st.selectbox(
        "Choose visualization type:",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram", "Box Plot"]
    )
    
    if viz_type == "Line Chart":
        y_column = st.selectbox("Select Y-axis:", ["sales", "users", "revenue"])
        fig = px.line(filtered_df, x='date', y=y_column, color='category')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Bar Chart":
        y_column = st.selectbox("Select Y-axis:", ["sales", "users", "revenue"])
        fig = px.bar(filtered_df, x='category', y=y_column)
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Scatter Plot":
        x_column = st.selectbox("Select X-axis:", ["sales", "users", "revenue"])
        y_column = st.selectbox("Select Y-axis:", ["sales", "users", "revenue"])
        fig = px.scatter(filtered_df, x=x_column, y=y_column, color='category')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Histogram":
        column = st.selectbox("Select column:", ["sales", "users", "revenue"])
        fig = px.histogram(filtered_df, x=column, color='category')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "Box Plot":
        column = st.selectbox("Select column:", ["sales", "users", "revenue"])
        fig = px.box(filtered_df, x='category', y=column)
        st.plotly_chart(fig, use_container_width=True)
    
    # Data table
    st.subheader("📋 Data Table")
    st.dataframe(filtered_df, use_container_width=True)

elif page == "Interactive Tools":
    st.markdown('<h1 class="main-header">🛠️ Interactive Tools</h1>', unsafe_allow_html=True)
    
    # Calculator
    st.subheader("🧮 Calculator")
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number:", value=0.0)
        num2 = st.number_input("Enter second number:", value=0.0)
    
    with col2:
        operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])
        
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        st.metric("Result", result)
    
    st.markdown("---")
    
    # Random number generator
    st.subheader("🎲 Random Number Generator")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        min_val = st.number_input("Minimum value:", value=1, step=1)
    
    with col2:
        max_val = st.number_input("Maximum value:", value=100, step=1)
    
    with col3:
        count = st.number_input("Number of values:", value=5, min_value=1, max_value=100, step=1)
    
    if st.button("Generate Random Numbers"):
        random_numbers = [random.randint(min_val, max_val) for _ in range(count)]
        st.write("Generated numbers:", random_numbers)
        st.bar_chart(pd.DataFrame(random_numbers, columns=['Random Numbers']))
    
    st.markdown("---")
    
    # Text analyzer
    st.subheader("📝 Text Analyzer")
    text_input = st.text_area("Enter text to analyze:")
    
    if text_input:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            word_count = len(text_input.split())
            st.metric("Word Count", word_count)
        
        with col2:
            char_count = len(text_input)
            st.metric("Character Count", char_count)
        
        with col3:
            sentence_count = len([s for s in text_input.split('.') if s.strip()])
            st.metric("Sentence Count", sentence_count)

elif page == "About":
    st.markdown('<h1 class="main-header">ℹ️ About</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🚀 AIH-2025 Streamlit Webapp
    
    This is a simple Streamlit webapp created for the AIH-2025 project. It demonstrates various features including:
    
    - **Dashboard**: Key metrics and charts
    - **Data Visualization**: Interactive charts and filters
    - **Interactive Tools**: Calculator, random number generator, and text analyzer
    
    ### Features:
    - 📊 Real-time data visualization
    - 🔍 Interactive filtering and analysis
    - 🛠️ Useful tools and calculators
    - 📱 Responsive design
    
    ### Technologies Used:
    - **Streamlit**: Web framework
    - **Pandas**: Data manipulation
    - **Plotly**: Interactive visualizations
    - **NumPy**: Numerical computing
    
    ### Getting Started:
    1. Install dependencies: `pip install -r requirements.txt`
    2. Run the app: `streamlit run src/main.py`
    3. Open your browser and navigate to the provided URL
    
    ---
    
    *Created with ❤️ for AIH-2025*
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Made with Streamlit | AIH-2025</div>",
    unsafe_allow_html=True
) 