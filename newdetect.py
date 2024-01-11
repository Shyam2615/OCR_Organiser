from PIL import Image, ImageEnhance
import cv2
import os
import pytesseract
import numpy as np

# Function to print a text-based design
def print_design():
    print("*" * 50)
    print(" -->  Welcome to Directory Input  <-- ")
    print("*" * 50)

def enhance_and_ocr(image_path):
    # Enhance image to match Windows snapshot quality
    img = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Adjust contrast (you can tweak this value)
    
    # Convert to OpenCV format
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Pass enhanced image to Tesseract OCR
    detected_text = pytesseract.image_to_string(img_cv)
    
    return detected_text

def process_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory, filename)
            
            # Load the image
            img = Image.open(image_path)
            
            # Enhance the image using Pillow
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(2)  # Increase contrast (adjust as needed)
            
            # Convert Pillow image to OpenCV format
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            # Preprocess using OpenCV (e.g., resizing, thresholding)
            processed_img = cv2.resize(img_cv, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
            processed_img = cv2.threshold(processed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
            # Save the preprocessed image
            cv2.imwrite(f'preprocessed_{filename}', processed_img)
            
            # Use Tesseract OCR on the preprocessed image
            text = pytesseract.image_to_string(processed_img)
            print(f"Text detected in {filename}: {text}")

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print_design()
l = []
b = " "
for i in range(100):
    a = input("Enter the directory or x to exit: ")
    if a.upper() == 'X':
        break
    if a.upper() in ['C', 'D', 'E']:
        if a.upper() == 'C':
            b = 'C:\\'
        if a.upper() == 'D':
            b = 'D:\\'
        if a.upper() == 'E':
            b = 'E:\\'
    else:
        l.append(a)

a = b + '\\'.join(l)
print(a)

# Directory containing images
input_directory = a

# Rest of your code remains unchanged below this point
# ...


# Directory containing images
# The rest of your code remains unchanged below this point
# ...


# Rest of your code remains unchanged below this point
# ...

# Create folders for different categories
categories = ['maths', 'physics', 'other', 'c++']
for category in categories:
    os.makedirs(category, exist_ok=True)

# Text detection function using Tesseract OCR
def detect_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return None
    
    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

def check_tags(text):
    tags = ['maths', 'physics', 'c++']  # Add more tags as needed
    for tag in tags:
        if f'#{tag}' in text.lower():
            return tag
    return 'other'
#C:\Users\ab\Desktop\dir
for filename in os.listdir(input_directory):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_directory, filename)
        enhance_and_ocr(image_path)
        process_images(a)
        destination_directory = 'C:\\Users\\ab\\Desktop\\dir'
        # Call detect_text function with image_path argument
        detected_text = detect_text(image_path)
        
        if detected_text:
            # Check for specific tags in the detected text
            category = check_tags(detected_text)
            
            destination = os.path.join(destination_directory, category, filename)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            
            os.replace(image_path, destination)