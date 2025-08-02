# 🧹 Project Cleanup & Improvements TODO

## 📁 File Organization

### Files to Remove/Clean:
- [x] `test.env.txt` - Empty file, should be deleted ✅ **COMPLETED**
- [x] `generated_prd.md` - Old generated file, should be in .gitignore ✅ **COMPLETED** (added to .gitignore)
- [x] `generated_prd_2025-08-02_20-45.md` - Old generated file, should be in .gitignore ✅ **COMPLETED** (added to .gitignore)
- [x] `requirements.txt` - Keep only `requirements_minimal.txt` or rename ✅ **COMPLETED**
- [x] `run_app.py` - Conflicts with `streamlit_app.py`, decide which to keep ✅ **COMPLETED**

### Files to Consolidate:
- [x] Merge `README.md` and `README_STREAMLIT.md` into one comprehensive README ✅ **COMPLETED**
- [x] Decide between `src/main.py` and `streamlit_app.py` - keep only one ✅ **COMPLETED** (keeping streamlit_app.py for PRD generator)

## 🔧 Code Improvements

### Streamlit App:
- [x] Add error handling for file uploads ✅ **COMPLETED**
- [x] Add progress bars for long operations ✅ **COMPLETED**
- [ ] Improve UI/UX with better styling (layout adjusted - left column narrower)
- [x] Add file validation (check if files are actually .docx) ✅ **COMPLETED**
- [x] Add session state management for better user experience ✅ **COMPLETED**

### PRD Generator:
- [x] Add logging for debugging ✅ **COMPLETED**
- [x] Improve error messages ✅ **COMPLETED**
- [x] Add retry mechanism for API calls ✅ **COMPLETED**
- [ ] Add support for different output formats (PDF, DOCX)

## 📚 Documentation

### README Improvements:
- [x] Create unified README with all features ✅ **COMPLETED**
- [ ] Add screenshots of the application
- [x] Add troubleshooting section ✅ **COMPLETED**
- [x] Add development setup instructions ✅ **COMPLETED**
- [x] Add API documentation ✅ **COMPLETED**

## 🚀 Deployment

### Production Ready:
- [ ] Add proper environment variable handling
- [ ] Add configuration file
- [ ] Add logging configuration
- [ ] Add health check endpoints
- [ ] Add proper error pages

## 🧪 Testing

### Test Coverage:
- [ ] Add unit tests for PRD generator
- [ ] Add integration tests for Streamlit app
- [ ] Add test data files
- [ ] Add CI/CD pipeline

## 🔒 Security

### Security Improvements:
- [x] Add input validation ✅ **COMPLETED**
- [x] Add file size limits ✅ **COMPLETED**
- [ ] Add rate limiting
- [x] Add proper API key handling ✅ **COMPLETED** 