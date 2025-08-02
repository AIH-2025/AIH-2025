# 🏗️ PRD Generator - System Architecture

## 📊 **High-Level Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PRD Generator System                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   Frontend      │    │   Backend       │    │   External APIs     │   │
│  │   (Streamlit)   │◄──►│   (Python)      │◄──►│   (OpenAI GPT-4)   │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
│           │                       │                       │               │
│           ▼                       ▼                       ▼               │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   File Upload   │    │   PRD Generator │    │   AI Processing     │   │
│  │   (.docx files) │    │   (Core Logic)  │    │   (Content Gen.)    │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
│           │                       │                       │               │
│           ▼                       ▼                       ▼               │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   Validation    │    │   File Storage  │    │   Output Generation │   │
│  │   & Processing  │    │   (generated_prds/)│   │   (Markdown/Text)  │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 🔧 **Detailed Component Architecture**

### **1. Frontend Layer (Streamlit UI)**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Streamlit Frontend                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   File Upload   │    │   Progress      │    │   PRD Display       │   │
│  │   Components    │    │   Tracking      │    │   & Download        │   │
│  │                 │    │                 │    │                     │   │
│  │ • Context File  │    │ • Progress Bar  │    │ • Live Preview      │   │
│  │ • Transcript    │    │ • Status Text   │    │ • Download Buttons  │   │
│  │ • Validation    │    │ • Error Display │    │ • Session State     │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
│           │                       │                       │               │
│           ▼                       ▼                       ▼               │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   Error         │    │   Session       │    │   User              │   │
│  │   Handling      │    │   Management    │    │   Experience        │   │
│  │                 │    │                 │    │                     │   │
│  │ • File Validation│   │ • State Persist │    │ • Responsive Layout │   │
│  │ • API Errors    │    │ • Error States  │    │ • Real-time Updates│   │
│  │ • User Feedback │    │ • Data Caching  │    │ • Clean UI/UX      │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### **2. Backend Layer (Python Core)**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Python Backend                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   File          │    │   PRD           │    │   API               │   │
│  │   Processing    │    │   Generator     │    │   Integration       │   │
│  │                 │    │                 │    │                     │   │
│  │ • read_docx()   │    │ • generate_prd()│   │ • OpenAI Client     │   │
│  │ • Validation    │    │ • Prompt Gen.   │    │ • Retry Logic       │   │
│  │ • Error Check   │    │ • Content Proc. │    │ • Rate Limiting     │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
│           │                       │                       │               │
│           ▼                       ▼                       ▼               │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   Logging       │    │   File          │    │   Security          │   │
│  │   & Monitoring  │    │   Management    │    │   & Validation      │   │
│  │                 │    │                 │    │                     │   │
│  │ • Debug Logs    │    │ • Temp Files    │    │ • Input Validation  │   │
│  │ • Error Logs    │    │ • Cleanup       │    │ • File Size Limits  │   │
│  │ • Performance   │    │ • Storage       │    │ • API Key Security  │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### **3. Data Flow Architecture**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Data Flow Pipeline                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   Input     │───►│   Process   │───►│   Generate  │───►│   Output    │ │
│  │   Files     │    │   & Validate│    │   PRD       │    │   Files     │ │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
│         │                   │                   │                   │     │
│         ▼                   ▼                   ▼                   ▼     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │ .docx Files │    │ Text        │    │ AI          │    │ generated_prds/│ │
│  │ (Context &  │    │ Extraction  │    │ Processing  │    │ folder       │ │
│  │  Transcript)│    │ & Validation│    │ (GPT-4)     │    │ (Markdown)   │ │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 📁 **File Structure Architecture**

```
AIH-2025/
├── 📄 streamlit_app.py              # Main UI Application
├── 📁 src/
│   └── 📄 prd_generator.py         # Core Business Logic
├── 📁 generated_prds/               # Output Storage
│   └── 📄 .gitkeep                 # Git tracking
├── 📄 requirements_minimal.txt      # Dependencies
├── 📄 .env                         # Environment Variables
├── 📄 .gitignore                   # Git Rules
├── 📄 README.md                    # Documentation
└── 📄 ARCHITECTURE.md              # This file
```

## 🔄 **Process Flow Architecture**

### **1. User Interaction Flow**
```
User Uploads Files
        │
        ▼
┌─────────────────┐
│ File Validation │
│ • Type Check    │
│ • Size Check    │
│ • Content Check │
└─────────────────┘
        │
        ▼
┌─────────────────┐
│ Generate Button │
│ • Progress Bar  │
│ • Status Updates│
└─────────────────┘
        │
        ▼
┌─────────────────┐
│ AI Processing   │
│ • OpenAI API    │
│ • Retry Logic   │
└─────────────────┘
        │
        ▼
┌─────────────────┐
│ Display Results │
│ • Live Preview  │
│ • Download      │
└─────────────────┘
```

### **2. Technical Process Flow**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   External      │
│   (Streamlit)   │    │   (Python)      │    │   (OpenAI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ 1. File Upload  │───►│ 2. File Read    │───►│ 3. API Call     │
│ • Validation    │    │ • Text Extract  │    │ • GPT-4 Request │
│ • Error Check   │    │ • Content Parse │    │ • Response      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ 6. Display      │◄───│ 5. Save File    │◄───│ 4. Process      │
│ • Live Preview  │    │ • generated_prds/│   │ • Content       │
│ • Download      │    │ • Cleanup       │    │ • Format        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔧 **Technology Stack Architecture**

### **Frontend Technologies**
- **Streamlit**: Web framework for data applications
- **CSS**: Custom styling for UI components
- **Session State**: State management for user interactions

### **Backend Technologies**
- **Python**: Core programming language
- **OpenAI API**: AI content generation
- **python-docx**: Document processing
- **python-dotenv**: Environment management

### **Infrastructure**
- **File System**: Local storage for generated files
- **Temporary Files**: System temp directory for processing
- **Logging**: Python logging for debugging

## 🔒 **Security Architecture**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Security Layers                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐   │
│  │   Input         │    │   API           │    │   File              │   │
│  │   Validation    │    │   Security      │    │   Security          │   │
│  │                 │    │                 │    │                     │   │
│  │ • File Type     │    │ • API Key       │    │ • Size Limits       │   │
│  │ • File Size     │    │ • Rate Limiting │    │ • Type Validation   │   │
│  │ • Content Check │    │ • Retry Logic   │    │ • Cleanup           │   │
│  └─────────────────┘    └─────────────────┘    └─────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 📊 **Performance Architecture**

### **Optimization Strategies**
- **Caching**: Session state for user data
- **Retry Logic**: Exponential backoff for API calls
- **Progress Tracking**: Real-time user feedback
- **Memory Management**: Temporary file cleanup

### **Scalability Considerations**
- **Stateless Design**: Session-based state management
- **Modular Architecture**: Separated concerns
- **Error Handling**: Graceful failure recovery
- **Resource Management**: Proper cleanup procedures

## 🎯 **Deployment Architecture**

### **Local Development**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Developer     │    │   Local         │    │   OpenAI        │
│   Machine       │    │   Environment   │    │   API           │
│                 │    │                 │    │                 │
│ • Streamlit     │    │ • Python        │    │ • GPT-4         │
│ • Browser       │    │ • Dependencies  │    │ • API Key       │
│ • .env File     │    │ • Local Files   │    │ • Rate Limits   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Production Considerations**
- **Environment Variables**: Secure API key management
- **File Storage**: Organized output directory
- **Error Logging**: Comprehensive error tracking
- **User Feedback**: Clear status messages

---

**This architecture provides a robust, scalable, and maintainable foundation for the PRD Generator application.** 