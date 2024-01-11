import cv2
import os
import pytesseract

# Function to print a text-based design
def print_design():
    print("*" * 50)
    print(" -->  Welcome to Directory Input  <-- ")
    print("*" * 50)

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
categories = ['physics', 'maths', 'other']
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

# Organize images based on detected text
for filename in os.listdir(input_directory):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_directory, filename)
        
        # Call detect_text function with image_path argument
        detected_text = detect_text(image_path)
        
        if detected_text:
            # Process the detected text to categorize the image
            if 'physics' in detected_text.lower():
                category = 'physics'
            elif 'maths' in detected_text.lower():
                category = 'maths'
            else:
                category = 'other'
            
            destination = os.path.join(category, filename)
            os.makedirs(category, exist_ok=True)
            
            os.replace(image_path, destination)
