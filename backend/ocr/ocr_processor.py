import pytesseract
from PIL import Image
from .preprocessing import preprocess_image

def process_prescription_image(image_file):
    # Preprocess the image
    image = Image.open(image_file)
    processed_image = preprocess_image(image)
    
    # Extract text using Tesseract
    prescription_text = pytesseract.image_to_string(processed_image)
    return prescription_text
