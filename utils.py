# from PIL import Image
# def compress_image(input_image_path, quality=20):
#     # Open the image file
#     image = Image.open(input_image_path)
    
#     # Compress and save the image with the desired quality
#     image.save(input_image_path, quality=quality)

# # Example usage:
   
# input_path = "C:\\Users\\ab\\Desktop\\dir\\WhatsApp Image 2024-01-05 at 20.13.05_e6727faa.jpg"

# compress_image(input_path, quality=20) 


from PIL import Image

def resize_to_match_sample(sample_image_path, image_path):
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

# Example usag
sample_image_path = "C:\\Users\\ab\\Desktop\\dir\\maths\\Screenshot 2024-01-05 195103.png"  # Replacewith path to your sample image
other_image_path = "C:\\Users\\ab\\Desktop\\dir\\WhatsApp Image 2024-01-05 at 20.13.05_e6727faa.jpg"    # Replace with path to the image you want to resize

# resize_to_match_sample(sample_image_path, other_image_path)

def join():
    l=[]
    a = input("Enter dir")   
    b = a.split('\\')
    c = '\\\\'.join(b)
    
    #l.append(c)
    print(c)

join()