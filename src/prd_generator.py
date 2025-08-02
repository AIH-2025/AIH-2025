import os
import openai
from docx import Document
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
# def ensure_openai_api_key():
#     """
#     Ensure that the OpenAI API key is set in the environment variables.
#     """
#     api_key = os.getenv("OPENAI_API_KEY")  
#     print(f"Key-------------->...{api_key}") 


def read_docx(file_path):
    """
    Reads a .docx file and returns its text content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    doc = Document(file_path)
    full_text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text)


def generate_prd_prompt(context, transcript):
    """
    Generates a prompt to feed into the LLM using the provided context and transcript.
    """
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

    Structure the output in clean Markdown.
    """


def generate_prd(context_path, transcript_path, output_path="generated_prd.md"):
    """
    Main function to read files, generate the PRD, and save it to a Markdown file.
    """
    try:
        # Load content
        context_text = read_docx(context_path)
        transcript_text = read_docx(transcript_path)

        # Create prompt
        prompt = generate_prd_prompt(context_text, transcript_text)
        # Call OpenAI API
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in writing professional product requirement documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extract response
        prd_output = response.choices[0].message.content
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        # Save to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"{prd_output}_{timestamp}")

        print(f"PRD saved as '{output_path}'")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Paths to the input files
    CONTEXT_FILE = "./ProductIsLife-PRDTemplate.docx"
    TRANSCRIPT_FILE = "./Hackathon-ArtificialInstinct.docx"

    # Ensure OPENAI_API_KEY is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Please set the OPENAI_API_KEY environment variable.")
    else:
        generate_prd(CONTEXT_FILE, TRANSCRIPT_FILE)
