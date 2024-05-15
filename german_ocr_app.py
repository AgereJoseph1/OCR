import streamlit as st
from PIL import Image
import easyocr
from googletrans import Translator

# Load EasyOCR and Translator just once
reader = easyocr.Reader(['de'])
translator = Translator()

def recognize_and_translate(image):
    results = reader.readtext(image)
    extracted_text = " ".join([text[1] for text in results])
    translation = translator.translate(extracted_text, src='de', dest='en').text
    return extracted_text, translation

def save_uploaded_file(uploaded_file):
    try:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return uploaded_file.name
    except Exception as e:
        return None

st.title('German Text OCR and Translation')
st.write("Upload an image with German text, and it will be translated into English.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image_path = save_uploaded_file(uploaded_file)
    if image_path:
        image = Image.open(image_path)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        with st.spinner('Recognizing text and translating...'):
            extracted_text, translated_text = recognize_and_translate(image_path)
            st.success('Done!')
            st.subheader('Extracted Text')
            st.write(extracted_text)
            st.subheader('Translated Text')
            st.write(translated_text)
