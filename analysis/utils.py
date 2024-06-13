import cv2
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile

def process_image(image: InMemoryUploadedFile) -> dict:
    # Convert the uploaded image to a numpy array
    image_array = np.frombuffer(image.read(), np.uint8)
    # Decode the image
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Image data could not be decoded. Ensure the uploaded file is a valid image.")

    # Assuming the strip is vertically aligned and divided into 10 sections
    height = img.shape[0] // 10
    colors = {}
    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    
    for i in range(10):
        section = img[i * height:(i + 1) * height, :]
        avg_color = section.mean(axis=0).mean(axis=0)
        colors[labels[i]] = avg_color.tolist()
    
    return colors

