#!/usr/bin/env python3
"""
Startup script for the AIH-2025 Streamlit webapp.
This script can be used to run the application locally.
"""

import subprocess
import sys
import os

def main():
    """Main function to start the Streamlit app."""
    print("🚀 Starting AIH-2025 Streamlit Webapp...")
    print("📊 Dashboard will be available at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Change to the src directory
        os.chdir("src")
        
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("💡 Make sure you have installed the requirements:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main() 