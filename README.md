
# AI-Powered Commercial Vehicle Insurance API

This project provides an API to retrieve structured JSON data from commercial vehicle insurance documents, powered by Google Generative AI. The system accepts PDF files, extracts text, and uses a prompt stored in `prompt.txt` to generate a structured JSON response.

## Project Structure

```
/project
    /static
        /ai_prompt        # Folder for AI-related inputs (prompt.txt)
            prompt.txt    # The prompt template for generating structured JSON
        /test_documents   # Sample PDF for testing
            test_document1.pdf
            test_document2.pdf
    /app
        __init__.py       # Flask application factory
        routes.py         # Route definitions
        policy_details_retriever.py # Core logic to handle policy detail retrieval
        config_loader.py  # Utility to load the config.yaml file
        ai_client.py      # Interaction with Google Generative AI
        json_utils.py     # Utility functions for JSON parsing and logging
    config.yaml           # Configuration file
    app.py                # Application entry point
```

## Prerequisites

- Python 3.11 or above
- Install the required dependencies:

```bash
pip -r requirements.txt
```

## Configuration

### `config.yaml`

The `config.yaml` file contains the configuration required for the API, including user authentication, Google API key, file paths, and prompt file location.

```yaml
users:
  admin:
    password: "secret"
  user:
    password: "password"

google_api_key: "YOUR_GOOGLE_API_KEY"
static_file_path: "./static"
prompt_file_path: "./static/ai_prompt/prompt.txt"
```

- **google_api_key**: Your Google Generative AI API key.
- **static_file_path**: Path to store static files (e.g., PDF documents).
- **prompt_file_path**: Path to the `prompt.txt` file, which contains the prompt template for generating structured data.

### `prompt.txt`

The `prompt.txt` file contains the prompt used to generate structured JSON from PDF text. The prompt is loaded dynamically from the `ai_prompt` folder specified in `config.yaml`.

## Running the Application

1. Ensure the `config.yaml` is properly set up with the correct paths and API key.
2. Place your PDF files in the `static/test_documents` folder.
3. Run the Flask application:

```bash
python app.py
```

The application will start on `http://localhost:3000`.

## API Endpoints

### 1. Health Check

- **Endpoint**: `/submissionIntakeAPI/health`
- **Method**: `GET`
- **Description**: Returns a message indicating the API is running.

**Example Response**:

```json
{
    "message": "API is running"
}
```

### 2. Retrieve Policy Details

- **Endpoint**: `/submissionIntakeAPI/retrievePolicyDetails`
- **Method**: `POST`
- **Description**: Accepts a filename (PDF) in the request body, extracts text from the PDF, and generates structured JSON based on the prompt.
  
**Request Body**:

```json
{
    "fileName": "test_document1.pdf"
}
```

**Example Response**:

```json
{
    "policyNumber": "123456",
    "policyStartDate": "2024-01-01",
    "policyType": "Commercial Auto",
    "policyHolderName": "John Doe",
    ...
}
```

### Error Handling

If the file does not exist or the file extension is not `.pdf`, the API will return appropriate error messages:

- **Invalid file extension**:

```json
{
    "error": "Invalid file extension. Only .pdf files are allowed."
}
```

- **File not found**:

```json
{
    "error": "File not found."
}
```

## Logging

The application logs are handled using Python’s logging module. Logs are generated for successful actions (like file reads and API calls) and for errors.

## License

This project is licensed under the MIT License.
