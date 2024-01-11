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

from PIL import Image
import os

def resize_to_match_sample(sample_image_path, image_path):
    # Open the sample image and the target image
    sample_image = Image.open(sample_image_path)
    target_image = Image.open(image_path)

    # Get dimensions of the sample image
    sample_width, sample_height = sample_image.size

    # Resize the target image to match the sample image's dimensions
    resized_image = target_image.resize((sample_width, sample_height))

    # Replace the original image with the resized image
    os.remove(image_path)  # Remove original image
    resized_image.save(image_path)  # Save the resized image with the original path

# Example usage:

    # Open the sample image and the target image
    sample_image = Image.open(sample_image_path)
    target_image = Image.open(image_path)

    # Get dimensions of the sample image
    sample_width, sample_height = sample_image.size

    # Resize the target image to match the sample image's dimensions
    resized_image = target_image.resize((sample_width, sample_height))

    # Save the resized image
    resized_image.save('resized_image.png')  # Change the filename or path as needed
    # Alternatively, you can return the resized image object if you want to further process it


# def enhance_and_ocr(image_path):
    # Enhance image to match Windows snapshot quality
    # img = Image.open(image_path)
    # enhancer = ImageEnhance.Contrast(img)
    # img = enhancer.enhance(2)  # Adjust contrast (you can tweak this value)
    
    # # Convert to OpenCV format
    # img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # # Pass enhanced image to Tesseract OCR
    # detected_text = pytesseract.image_to_string(img_cv)
    
    # return detected_text

# from PIL import Image

 # Adjust quality (0-100) as needed


# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print_design()

a = input("Enter dir")   
b = a.split('\\')
c = '\\\\'.join(b)
# for i in range(100):
#     a = input("Enter the directory or x to exit: ")
#     if a.upper() == 'X':
#         break
#     if a.upper() in ['C', 'D', 'E']:
#         if a.upper() == 'C':
#             b = 'C:\\'
#         if a.upper() == 'D':
#             b = 'D:\\'
#         if a.upper() == 'E':
#             b = 'E:\\'
#     else:
#         l.append(a)

# a = b + '\\'.join(l)
# print(a)

# Directory containing images
input_directory = c

# Rest of your code remains unchanged below this point
# ...


# Directory containing images
# The rest of your code remains unchanged below this point
# ...


# Rest of your code remains unchanged below this point
# ...

# Create folders for different categories
categories = ['python','node', 'struct', 'other']
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
sample_image_path = "C:\\Users\\ab\\Desktop\\dir\\maths\\Screenshot 2024-01-05 195103.png"  # Replacewith path to your sample image
for filename in os.listdir(input_directory):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_directory, filename)
        # Example usag
        other_image_path = image_path   # Replace with path to the image you want to resize

        resize_to_match_sample(sample_image_path, other_image_path)
        print(f"Processing image: {image_path}")  # Add this line for debugging
        
        # Call detect_text function with image_path argument
        # enhance_and_ocr(image_path)
        detected_text = detect_text(image_path)
        # Set a default destination directory
        destination_directory = 'C:\\Users\\ab\\Desktop\\dir'

        if detected_text:
            # Process the detected text to categorize the image
            if 'physics' in detected_text.lower():
                category = 'physics'
            elif 'maths' in detected_text.lower():
                category = 'maths'
            elif 'python' in detected_text.lower():
                category = 'python'
            else:
                category = 'other'
            
            destination = os.path.join(destination_directory, category, filename)
            print(f"Moving to: {destination}")  # Add this line for debugging
            
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            os.replace(image_path, destination)
