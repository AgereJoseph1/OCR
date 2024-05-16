import streamlit as st 
import os
import io
from google.cloud import vision
from googletrans import Translator
import time

st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -20px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4267B2;">
    <a class="navbar-brand" href="#"  target="_blank">Redox OCR</a>  
    </nav>
""",
    unsafe_allow_html=True,
)

st.markdown(f"<div class ='card alert alert-success' style='color:black'>Optical Character recognition Software</div>",unsafe_allow_html=True)




file_upload = st.file_uploader("Upload Image file")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def detect_text(image_path):
    """Detects text in an image using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    start_time = time.time()
    response = client.text_detection(image=image)
    end_time = time.time()
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    if texts:
        return texts[0].description, end_time - start_time
    else:
        return None, end_time - start_time

def translate_text(text, src='de', dest='en'):
    """Translates text from source language to destination language using Google Translate API."""
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def detect_and_translate(image_path):
    """Detects text in an image and translates it from German to English."""
    german_text, detection_time = detect_text(image_path)
    with st.expander("Original Image"):
        st.image(file_upload.name)

    if german_text:

        with st.expander("Metrics"):
            col1, col2, col3 = st.columns(3)
            col1.metric("Detection Time", detection_time, "secs")
 
        with st.expander("German Text"):
            st.markdown(f"<span class='note card alert-warning ' style='color: black'>{german_text}</span>",unsafe_allow_html=True)
        
        print("")
        english_text = translate_text(german_text)
        with st.expander("Translated Text"):
            st.markdown(f"<span class='note card' style='color: black'>{english_text}</span>",unsafe_allow_html=True)
        
    else:
        st.write("No text detected.")


if st.button("submit"):
    with st.spinner("Loading..."):
        detect_and_translate(file_upload.name)
