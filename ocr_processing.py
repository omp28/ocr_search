import pytesseract
import cv2
from PIL import Image

def perform_ocr(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    text = pytesseract.image_to_string(img_rgb, lang='eng+hin')  
    return text

def search_keyword(extracted_text, keyword):
    results = [line for line in extracted_text.split('\n') if keyword.lower() in line.lower()]
    return results
