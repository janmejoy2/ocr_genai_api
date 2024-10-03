import google.generativeai as genai
from .config_loader import load_config
from .logger import logger

# Load configuration
config = load_config()
GOOGLE_API_KEY = config['google_api_key']
PROMPT_FILE_PATH = config['prompt_file_path']

if not GOOGLE_API_KEY:
    logger.error("Google API Key not found in config.yaml")
    raise ValueError("Google API Key not found in config.yaml")

if not PROMPT_FILE_PATH:
    logger.error("Prompt file path not found in config.yaml")
    raise ValueError("Prompt file path not found in config.yaml")

genai.configure(api_key=GOOGLE_API_KEY)


def read_prompt_template():
    """
    Function to read the prompt template from the configured file.
    """
    try:
        with open(PROMPT_FILE_PATH, 'r') as file:
            prompt_template = file.read()
            logger.info(f"Successfully read prompt template from {PROMPT_FILE_PATH}")
            return prompt_template
    except Exception as e:
        logger.error(f"Error reading {PROMPT_FILE_PATH}: {e}")
        raise


def generate_structured_json_from_pdf_text(pdf_text):
    """
    Send the extracted PDF text to Google Generative AI and get structured JSON response.
    """
    # Read the prompt template from the prompt file
    prompt_template = read_prompt_template()

    # Insert the extracted PDF text into the prompt
    prompt = f"{prompt_template}\n\nText:\n{pdf_text}"

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-002')
        response = model.generate_content(prompt)
        logger.info("Successfully generated structured data from AI.")
        return response.text.strip()
    except Exception as e:
        logger.error(f"Error in generating structured data from AI: {e}")
        return None
