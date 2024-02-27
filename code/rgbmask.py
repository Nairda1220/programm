import cv2
import numpy as np
from PIL import Image

def process_image(image_path):
    # Open the original image
    original_image = cv2.imread(image_path)

    # Open the image with PIL for RGB filtering
    image = Image.open(image_path)
    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))

            if not (r > 120 and g < r - 70 and b < r - 70):
                image.putpixel((i, j), (255, 255, 255))

    # Convert processed image to grayscale
    img_gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_img, threshold1=30, threshold2=100)

    # Use closing operation to connect small gaps
    kernel = np.ones((5,5),np.uint8)
    closing_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(closing_edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    max_contour = max(contours, key=cv2.contourArea)

    # Draw a bounding rectangle around the largest contour on the original image
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(original_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save the image with the bounding rectangle
    cv2.imwrite('contour_image.png', original_image)

process_image('helmet.jpg')
