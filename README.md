# Redox OCR

Redox OCR is an Optical Character Recognition (OCR) software built using Streamlit, Google Cloud Vision API, and Google Translate API. It allows users to upload an image file containing text, detects the text within the image using Google Cloud Vision API, and translates it from German to English using Google Translate API.

## Features

- **Text Detection**: Detects text within uploaded image files.
- **Translation**: Translates the detected text from German to English.
- **User Interface**: Provides a simple user interface for uploading images and viewing detected and translated text.

## Installation

To run Redox OCR locally, you need to have Python installed on your system. You can then install the required dependencies using pip:

```bash
pip install streamlit google-cloud-vision googletrans
```

Ensure you have the `credentials.json` file containing your Google Cloud credentials.

## Usage

1. Clone the repository or copy the provided code snippet into a Python script.
2. Ensure your Google Cloud credentials are set by pointing to the `credentials.json` file.
3. Run the script using the following command:

```bash
streamlit run your_script.py
```

4. Access the web application in your browser.
5. Upload an image file containing text.
6. Click the "Submit" button to detect and translate the text.

## Dependencies

- **Streamlit**: A Python library for building web applications.
- **Google Cloud Vision API**: Used for detecting text within images.
- **Google Translate API**: Used for translating text from German to English.

## Limitations

- Redox OCR currently supports only German to English translation.
- The accuracy of text detection and translation may vary depending on the quality and clarity of the uploaded images.

## Acknowledgments

Redox OCR utilizes the following open-source libraries:

- Streamlit
- Google Cloud Vision API
- Google Translate API

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project or customize it according to your needs! If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out.
