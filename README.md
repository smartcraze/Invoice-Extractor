# Multilanguage Invoice Extractor

A Streamlit application to extract and understand information from invoice images using Google's Generative AI.

## Features

- Upload invoice images in JPG, JPEG, or PDF format.
- Extract and answer questions based on the uploaded invoice image using Gemini Pro Vision.

## Requirements

- Python 3.7+
- Streamlit
- python-dotenv
- Pillow (PIL)
- google-generativeai

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/multilanguage-invoice-extractor.git
    cd multilanguage-invoice-extractor
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an invoice image and input your prompt to get the response based on the uploaded invoice image.

## Project Structure
```multilanguage-invoice-extractor/
├── app.py
├── requirements.txt
├── .env
└── README.md
```
- `app.py`: Main application file containing the Streamlit app code.
- `requirements.txt`: List of dependencies required for the project.
- `.env`: Environment file to store the Google API key.
- `README.md`: Project documentation.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pillow](https://python-pillow.org/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
