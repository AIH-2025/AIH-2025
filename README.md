# 🚀 AIH-2025 Streamlit Webapp

A modern, interactive web application built with Streamlit for data visualization and analysis.

## 📋 Features

- **📊 Dashboard**: Real-time metrics and interactive charts
- **📈 Data Visualization**: Multiple chart types with filtering capabilities
- **🛠️ Interactive Tools**: Calculator, random number generator, and text analyzer
- **📱 Responsive Design**: Works on desktop and mobile devices
- **🐳 Docker Support**: Easy deployment with Docker

## 🏗️ Project Structure

```
AIH-2025/
├── src/
│   ├── main.py              # Main Streamlit application
│   ├── utils.py             # Utility functions
│   └── .streamlit/
│       └── config.toml      # Streamlit configuration
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── run_app.py              # Local startup script
└── README.md               # This file
```

## 🚀 Quick Start

### Option 1: Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   # Method 1: Using the startup script
   python run_app.py
   
   # Method 2: Direct streamlit command
   streamlit run src/main.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:8501`

### Option 2: Docker Deployment

1. **Build the Docker image:**
   ```bash
   docker build -t aih-2025 .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8501:8501 aih-2025
   ```

3. **Access the application:**
   Navigate to `http://localhost:8501`

## 📊 Application Pages

### Dashboard
- Key performance metrics
- Interactive charts and graphs
- Real-time data visualization

### Data Visualization
- Multiple chart types (Line, Bar, Scatter, Histogram, Box Plot)
- Date range filtering
- Category-based filtering
- Interactive data table

### Interactive Tools
- **Calculator**: Basic arithmetic operations
- **Random Number Generator**: Generate random numbers with visualization
- **Text Analyzer**: Word, character, and sentence counting

### About
- Project information and documentation
- Technology stack details
- Getting started guide

## 🛠️ Technologies Used

- **Streamlit**: Web framework for data applications
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Plotly**: Interactive visualizations
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical data visualization

## 🔧 Configuration

The application can be customized through the following files:

- `src/.streamlit/config.toml`: Streamlit theme and server settings
- `src/main.py`: Main application logic
- `src/utils.py`: Utility functions and helpers

## 📈 Sample Data

The application uses generated sample data with the following characteristics:
- **Time Series**: Daily data from 2024
- **Metrics**: Sales, Users, Revenue
- **Categories**: A, B, C with different distributions
- **Features**: Trends, seasonality, and realistic noise

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Kill existing process on port 8501
   lsof -ti:8501 | xargs kill -9
   ```

2. **Dependencies not found:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Docker build fails:**
   ```bash
   # Clean Docker cache
   docker system prune -a
   docker build --no-cache -t aih-2025 .
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

## 📄 License

This project is created for AIH-2025 hackathon.

---

**Made with ❤️ for AIH-2025**