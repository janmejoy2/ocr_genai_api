import json
import ast
from .logger import logger


def parse_ai_response(response_text):
    """
    Parse the response text from Google Generative AI into structured JSON format.
    """
    formatted_string = response_text.replace('```json', '', 1).replace('```', '', 1).strip()

    try:
        parsed_json = json.loads(formatted_string)
        logger.info("Successfully parsed AI response into JSON.")
    except json.JSONDecodeError as e:
        try:
            parsed_json = ast.literal_eval(formatted_string)
        except (ValueError, SyntaxError) as ve:
            logger.error(f"Invalid JSON format: {ve}")
            return f"Invalid JSON: {ve}"

    return parsed_json
