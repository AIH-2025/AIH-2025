import streamlit as st
import os
import tempfile
from datetime import datetime
import sys
import logging
from typing import Optional
import time
sys.path.append('src')
from prd_generator import generate_prd, read_docx

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="PRD Generator",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .upload-section {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .generate-button {
        background-color: #1f77b4;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
    }
    .download-button {
        background-color: #28a745;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        font-size: 1rem;
    }
    .prd-display {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        max-height: 600px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

def validate_docx_file(uploaded_file) -> bool:
    """Validate if uploaded file is actually a .docx file"""
    if uploaded_file is None:
        return False
    
    # Check file extension
    if not uploaded_file.name.lower().endswith('.docx'):
        return False
    
    # Check file size (max 10MB)
    if uploaded_file.size > 10 * 1024 * 1024:
        return False
    
    return True

def main():
    # Initialize session state
    if 'prd_content' not in st.session_state:
        st.session_state.prd_content = None
    if 'prd_filename' not in st.session_state:
        st.session_state.prd_filename = None
    if 'generation_error' not in st.session_state:
        st.session_state.generation_error = None
    
    # Header
    st.markdown('<h1 class="main-header">📋 PRD Generator</h1>', unsafe_allow_html=True)
    
    # Check for OpenAI API key
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("⚠️ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        st.stop()
    
    # Create two columns for the layout - left column narrower for uploads
    col1, col2 = st.columns([0.4, 0.6])
    
    with col1:
        st.markdown("### 📁 Upload Files")
        
        # File upload section
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        
        # Context file upload
        st.markdown("**PRD Template/Context File:**")
        context_file = st.file_uploader(
            "Choose a .docx file for PRD template/context",
            type=['docx'],
            key="context_upload"
        )
        
        # Validate context file
        if context_file and not validate_docx_file(context_file):
            st.error("❌ Invalid context file. Please upload a valid .docx file (max 10MB).")
            context_file = None
        
        # Transcript file upload
        st.markdown("**Meeting Transcript File:**")
        transcript_file = st.file_uploader(
            "Choose a .docx file for meeting transcript",
            type=['docx'],
            key="transcript_upload"
        )
        
        # Validate transcript file
        if transcript_file and not validate_docx_file(transcript_file):
            st.error("❌ Invalid transcript file. Please upload a valid .docx file (max 10MB).")
            transcript_file = None
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Generate button
        if context_file and transcript_file:
            if st.button("🚀 Generate PRD", key="generate_btn", use_container_width=True):
                # Clear previous errors
                st.session_state.generation_error = None
                
                # Progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    # Step 1: Creating temporary files
                    status_text.text("📁 Creating temporary files...")
                    progress_bar.progress(20)
                    
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_context:
                        tmp_context.write(context_file.getvalue())
                        context_path = tmp_context.name
                    
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_transcript:
                        tmp_transcript.write(transcript_file.getvalue())
                        transcript_path = tmp_transcript.name
                    
                    # Step 2: Generating PRD
                    status_text.text("🤖 Generating PRD with AI...")
                    progress_bar.progress(50)
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
                    output_filename = f"generated_prds/generated_prd_{timestamp}.md"
                    
                    # Call the generate_prd function with retry mechanism
                    max_retries = 3
                    for attempt in range(max_retries):
                        try:
                            generate_prd(context_path, transcript_path, output_filename)
                            break
                        except Exception as e:
                            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                            if attempt == max_retries - 1:
                                raise e
                            time.sleep(2)  # Wait before retry
                    
                    # Step 3: Reading generated PRD
                    status_text.text("📄 Reading generated PRD...")
                    progress_bar.progress(80)
                    
                    with open(output_filename, 'r', encoding='utf-8') as f:
                        prd_content = f.read()
                    
                    # Step 4: Storing in session state
                    st.session_state.prd_content = prd_content
                    st.session_state.prd_filename = output_filename
                    
                    # Clean up temporary files
                    os.unlink(context_path)
                    os.unlink(transcript_path)
                    
                    progress_bar.progress(100)
                    status_text.text("✅ PRD generated successfully!")
                    time.sleep(1)  # Show success message briefly
                    
                    st.success("✅ PRD generated successfully!")
                    
                except Exception as e:
                    error_msg = f"❌ Error generating PRD: {str(e)}"
                    logger.error(error_msg)
                    st.session_state.generation_error = error_msg
                    st.error(error_msg)
                finally:
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
        else:
            st.info("📝 Please upload both context and transcript files to generate PRD.")
    
    with col2:
        st.markdown("### 📄 Generated PRD")
        
        # Show error if generation failed
        if st.session_state.generation_error:
            st.error(st.session_state.generation_error)
        
        if st.session_state.prd_content:
            # Display the PRD content
            st.markdown('<div class="prd-display">', unsafe_allow_html=True)
            st.markdown(st.session_state.prd_content)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Download section
            st.markdown("---")
            st.markdown("### 💾 Download PRD")
            
            # Create download buttons
            prd_content = st.session_state.prd_content
            filename = st.session_state.prd_filename or 'generated_prd.md'
            
            col_dl1, col_dl2 = st.columns(2)
            
            with col_dl1:
                st.download_button(
                    label="📥 Download as Markdown",
                    data=prd_content,
                    file_name=filename,
                    mime="text/markdown",
                    use_container_width=True
                )
            
            with col_dl2:
                st.download_button(
                    label="📥 Download as Text",
                    data=prd_content,
                    file_name=filename.replace('.md', '.txt'),
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.info("📋 Generated PRD will appear here after clicking the Generate button.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        PRD Generator - Powered by OpenAI GPT-4
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 