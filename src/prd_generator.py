import os
import openai
from docx import Document
from dotenv import load_dotenv
from datetime import datetime
import logging
import time
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
# def ensure_openai_api_key():
#     """
#     Ensure that the OpenAI API key is set in the environment variables.
#     """
#     api_key = os.getenv("OPENAI_API_KEY")  
#     print(f"Key-------------->...{api_key}") 


def read_docx(file_path: str) -> str:
    """
    Reads a .docx file and returns its text content.
    
    Args:
        file_path: Path to the .docx file
        
    Returns:
        str: Text content of the document
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a valid .docx
    """
    logger.info(f"Reading document: {file_path}")
    
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        doc = Document(file_path)
        full_text = [para.text for para in doc.paragraphs if para.text.strip()]
        content = "\n".join(full_text)
        
        if not content.strip():
            logger.warning(f"Document appears to be empty: {file_path}")
            raise ValueError(f"Document is empty or contains no readable text: {file_path}")
        
        logger.info(f"Successfully read document with {len(content)} characters")
        return content
        
    except Exception as e:
        logger.error(f"Error reading document {file_path}: {str(e)}")
        raise ValueError(f"Invalid .docx file or corrupted document: {file_path}")


def generate_prd_prompt(context: str, transcript: str) -> str:
    """
    Generates a prompt to feed into the LLM using the provided context and transcript.
    
    Args:
        context: PRD template/context text
        transcript: Meeting transcript text
        
    Returns:
        str: Formatted prompt for the LLM
    """
    logger.info("Generating PRD prompt")
    
    return f"""
    You are a product manager assistant. Your task is to generate a Product Requirements Document (PRD).

    Use the following PRD schema/context as a base:

    --- Start of Context ---
    {context}
    --- End of Context ---

    Based on the following meeting transcript:

    --- Start of Transcript ---
    {transcript}
    --- End of Transcript ---

    Generate a comprehensive PRD based on the context and discussed items in the transcript. Include sections like:
    - Product Goal
    - Stakeholders
    - Features and Functionalities
    - User Stories
    - Technical Requirements
    - Constraints
    - Milestones
    - Acceptance Criteria

    Structure the output in clean Markdown with proper headings and formatting.
    """


def generate_prd(context_path: str, transcript_path: str, output_path: str = "generated_prd.md") -> str:
    """
    Main function to read files, generate the PRD, and save it to a Markdown file.
    
    Args:
        context_path: Path to the context/template file
        transcript_path: Path to the transcript file
        output_path: Path where to save the generated PRD
        
    Returns:
        str: Generated PRD content
        
    Raises:
        Exception: If any step in the process fails
    """
    logger.info(f"Starting PRD generation: {context_path}, {transcript_path} -> {output_path}")
    
    try:
        # Step 1: Load content
        logger.info("Loading document content...")
        context_text = read_docx(context_path)
        transcript_text = read_docx(transcript_path)
        
        logger.info(f"Context length: {len(context_text)} chars, Transcript length: {len(transcript_text)} chars")

        # Step 2: Create prompt
        prompt = generate_prd_prompt(context_text, transcript_text)
        
        # Step 3: Call OpenAI API with retry mechanism
        logger.info("Calling OpenAI API...")
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert in writing professional product requirement documents."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=4000  # Limit response length
                )
                break
            except openai.RateLimitError as e:
                logger.warning(f"Rate limit hit, attempt {attempt + 1}/{max_retries}")
                if attempt == max_retries - 1:
                    raise e
                time.sleep(2 ** attempt)  # Exponential backoff
            except openai.APIError as e:
                logger.error(f"OpenAI API error: {str(e)}")
                raise e

        # Step 4: Extract and process response
        prd_output = response.choices[0].message.content
        
        if not prd_output.strip():
            raise ValueError("Generated PRD is empty")
        
        logger.info(f"Generated PRD with {len(prd_output)} characters")
        
        # Step 5: Save to file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        final_content = f"# Generated PRD - {timestamp}\n\n{prd_output}"
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logger.info(f"Created directory: {output_dir}")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        logger.info(f"PRD saved successfully as '{output_path}'")
        return final_content

    except Exception as e:
        logger.error(f"Error generating PRD: {str(e)}")
        raise Exception(f"Failed to generate PRD: {str(e)}")


if __name__ == "__main__":
    # Paths to the input files
    CONTEXT_FILE = "./ProductIsLife-PRDTemplate.docx"
    TRANSCRIPT_FILE = "./Hackathon-ArtificialInstinct.docx"

    # Ensure OPENAI_API_KEY is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Please set the OPENAI_API_KEY environment variable.")
    else:
        generate_prd(CONTEXT_FILE, TRANSCRIPT_FILE)
