# 📋 PRD Generator - AI-Powered Product Requirements Document Creator

A modern Streamlit web application that generates comprehensive Product Requirements Documents (PRD) from meeting transcripts and PRD templates using OpenAI's GPT-4.

## 🚀 Features

- **📁 File Upload**: Upload PRD template/context and meeting transcript files (.docx format)
- **🤖 AI-Powered Generation**: Uses OpenAI GPT-4 for intelligent PRD creation
- **📄 Live Preview**: View generated PRD in real-time on the right side
- **💾 Download Options**: Download PRD as Markdown or Text files
- **🎨 Modern UI**: Clean, responsive interface with professional styling
- **⚡ One-Click Generation**: Simple workflow with minimal user interaction

## 🏗️ Project Structure

```
AIH-2025/
├── streamlit_app.py          # Main Streamlit application
├── src/
│   └── prd_generator.py     # Core PRD generation logic
├── requirements_minimal.txt  # Python dependencies
├── .env                     # Environment variables (create this)
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements_minimal.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# For Windows (PowerShell)
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

# For Windows (Command Prompt)
echo OPENAI_API_KEY=your_openai_api_key_here > .env
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 3. Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📖 Usage Guide

### Step 1: Upload Files
- **PRD Template/Context File**: Upload a .docx file containing your PRD template or context
- **Meeting Transcript File**: Upload a .docx file containing the meeting transcript

### Step 2: Generate PRD
- Click the "🚀 Generate PRD" button
- Wait for the AI to process and generate the document

### Step 3: View & Download
- View the generated PRD on the right side
- Download the PRD as Markdown (.md) or Text (.txt) file

## 🔧 Technical Details

### Dependencies
- **streamlit**: Web framework for the UI
- **openai**: OpenAI API integration
- **python-docx**: Microsoft Word document processing
- **python-dotenv**: Environment variable management

### File Requirements
- **Input Files**: Must be .docx format
- **Output**: Generated as Markdown with timestamp in `generated_prds/` folder
- **API**: Requires OpenAI API key with GPT-4 access

## 🛠️ Development

### Local Development Setup

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements_minimal.txt`
3. **Set up environment**: Create `.env` file with your API key
4. **Run development server**: `streamlit run streamlit_app.py`

### Code Structure

- `streamlit_app.py`: Main Streamlit application with UI components
- `src/prd_generator.py`: Core logic for PRD generation
- `requirements_minimal.txt`: Minimal dependencies for the application

## 🔒 Security & Best Practices

- **API Key Security**: Store your OpenAI API key in the `.env` file (not in code)
- **File Validation**: Application validates file types and handles errors gracefully
- **Temporary Files**: Generated files are cleaned up automatically
- **Error Handling**: Comprehensive error messages and validation

## 🐛 Troubleshooting

### Common Issues

**OpenAI API Key Error**
```
⚠️ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.
```
**Solution**: Create a `.env` file with your API key

**File Upload Issues**
- Ensure files are in .docx format
- Check file size (should be reasonable for processing)

**Generation Errors**
- Verify your internet connection
- Check that your OpenAI API key is valid
- Ensure you have GPT-4 access in your OpenAI account

### Getting Help

1. Check that all dependencies are installed correctly
2. Verify your OpenAI API key is working
3. Ensure input files are valid .docx format
4. Check the browser console for any JavaScript errors

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Review the error messages in the application
- Ensure all setup steps have been completed correctly

---

**Built with ❤️ using Streamlit and OpenAI GPT-4**