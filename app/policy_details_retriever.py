from flask import request, jsonify
import os
from .ai_client import generate_structured_json_from_pdf_text
from .json_utils import parse_ai_response
from .config_loader import load_config
from .logger import logger
from PyPDF2 import PdfReader

# Load config to get static file path
config = load_config()
STATIC_FILE_PATH = config['static_file_path']


def retrieve_policy_details_route():
    try:
        # Extract filename from request body
        data = request.get_json()
        file_name = data.get("fileName")

        if not file_name:
            logger.error("Filename is missing in request body.")
            return jsonify({"error": "Filename is required in the request body."}), 400

        # Ensure the file has a .pdf extension
        if not file_name.lower().endswith('.pdf'):
            logger.error(f"Invalid file extension: {file_name}")
            return jsonify({"error": "Invalid file extension. Only .pdf files are allowed."}), 400

        # Set the file path dynamically from config.yaml
        file_path = os.path.join(STATIC_FILE_PATH, file_name)

        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return jsonify({"error": "File not found."}), 404

        # Read the PDF
        pdf_text = read_pdf(file_path)

        if not pdf_text:
            logger.error("Failed to extract text from PDF.")
            return jsonify({"error": "Failed to extract text from PDF."}), 500

        # Generate structured data from AI
        ai_response = generate_structured_json_from_pdf_text(pdf_text)

        if not ai_response:
            logger.error("Failed to generate structured data from AI.")
            return jsonify({"error": "Failed to generate structured data from AI."}), 500

        # Parse AI response
        json_response = parse_ai_response(ai_response)
        logger.info("Successfully retrieved policy details.")
        return jsonify(json_response)

    except Exception as e:
        logger.error(f"Error in retrieve_policy_details: {e}")
        return jsonify({"error": f"Failed to retrieve policy details: {e}"})


def read_pdf(file_path):
    """
    Function to read and extract text from PDF.
    """
    try:
        pdf_reader = PdfReader(file_path)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        logger.info(f"Successfully read PDF from {file_path}")
        return pdf_text
    except Exception as e:
        logger.error(f"Error in reading PDF: {e}")
        return None
