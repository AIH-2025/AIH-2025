import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

def generate_time_series_data(start_date='2024-01-01', end_date='2024-12-31', freq='D'):
    """
    Generate sample time series data for demonstration purposes.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        freq (str): Frequency of data points ('D' for daily, 'H' for hourly, etc.)
    
    Returns:
        pd.DataFrame: DataFrame with time series data
    """
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    
    # Generate realistic data with trends and seasonality
    n_points = len(dates)
    
    # Base trends
    trend = np.linspace(0, 100, n_points)
    seasonal = 50 * np.sin(2 * np.pi * np.arange(n_points) / 365)  # Yearly seasonality
    weekly = 20 * np.sin(2 * np.pi * np.arange(n_points) / 7)      # Weekly seasonality
    
    # Generate different metrics
    sales = 1000 + trend + seasonal + weekly + np.random.normal(0, 50, n_points)
    users = 500 + 0.5 * trend + 0.3 * seasonal + np.random.normal(0, 30, n_points)
    revenue = 5000 + 5 * trend + 2 * seasonal + np.random.normal(0, 200, n_points)
    
    # Ensure positive values
    sales = np.maximum(sales, 0)
    users = np.maximum(users, 0)
    revenue = np.maximum(revenue, 0)
    
    data = {
        'date': dates,
        'sales': sales,
        'users': users,
        'revenue': revenue,
        'category': np.random.choice(['A', 'B', 'C'], n_points, p=[0.4, 0.35, 0.25])
    }
    
    return pd.DataFrame(data)

def create_summary_stats(df):
    """
    Create summary statistics for a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame
    
    Returns:
        dict: Dictionary containing summary statistics
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    summary = {}
    for col in numeric_cols:
        summary[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max(),
            'sum': df[col].sum()
        }
    
    return summary

def create_metric_card(title, value, prefix="", suffix="", delta=None):
    """
    Create a formatted metric card for display.
    
    Args:
        title (str): Title of the metric
        value (float/int): Value to display
        prefix (str): Prefix for the value (e.g., "$")
        suffix (str): Suffix for the value (e.g., "%")
        delta (float, optional): Delta value for change indicator
    
    Returns:
        str: HTML formatted metric card
    """
    if isinstance(value, (int, float)):
        if value >= 1e6:
            formatted_value = f"{value/1e6:.1f}M"
        elif value >= 1e3:
            formatted_value = f"{value/1e3:.1f}K"
        else:
            formatted_value = f"{value:,.0f}"
    else:
        formatted_value = str(value)
    
    html = f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <h2>{prefix}{formatted_value}{suffix}</h2>
    </div>
    """
    
    return html

def create_interactive_chart(df, chart_type="line", x_col="date", y_col="sales", 
                           color_col=None, title="Chart"):
    """
    Create an interactive Plotly chart.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        chart_type (str): Type of chart ('line', 'bar', 'scatter', 'histogram')
        x_col (str): Column name for x-axis
        y_col (str): Column name for y-axis
        color_col (str, optional): Column name for color coding
        title (str): Chart title
    
    Returns:
        plotly.graph_objects.Figure: Plotly figure object
    """
    if chart_type == "line":
        fig = px.line(df, x=x_col, y=y_col, color=color_col, title=title)
    elif chart_type == "bar":
        fig = px.bar(df, x=x_col, y=y_col, color=color_col, title=title)
    elif chart_type == "scatter":
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col, title=title)
    elif chart_type == "histogram":
        fig = px.histogram(df, x=y_col, color=color_col, title=title)
    else:
        fig = px.line(df, x=x_col, y=y_col, title=title)
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True
    )
    
    return fig

def calculate_percentage_change(current, previous):
    """
    Calculate percentage change between two values.
    
    Args:
        current (float): Current value
        previous (float): Previous value
    
    Returns:
        float: Percentage change
    """
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100 