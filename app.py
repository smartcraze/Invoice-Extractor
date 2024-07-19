from dotenv import load_dotenv
import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai 

load_dotenv()  ## load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Vision 
model = genai.GenerativeModel('gemini-1.5-flash')

def GetGeminiResponse(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

## Bytes data image processing
def inputImageSetup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit configuration

st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.header("Multilanguage Invoice Extractor")
Yourinput_prompt = st.text_input("Input prompt:", key="input_prompt")
upload_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "pdf","png"])

## Display image
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell Me")
input_prompt = """
You are an expert in understanding invoices. We will upload an image of an invoice and you will have to answer any question based on the uploaded invoice image.
"""

## If submit is clicked
if submit:
    imageData = inputImageSetup(upload_file)
    response = GetGeminiResponse(input_prompt, imageData, Yourinput_prompt)
    st.subheader("The response is:")
    st.write(response)
