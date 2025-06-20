# demo.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('eminem.jpg')

if img is None:
    print("Error: Image not found.")
    exit()

# Add white patch (for fun or testing)
img[206:236, 224:313] = [255, 255, 255]

# Add text to the image
cv2.putText(img, 'The Real Slim Shady',
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (250, 250, 250),
            2)

# Convert image formats
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show with matplotlib
plt.figure(figsize=(6, 6))
plt.imshow(img_rgb)
plt.title('Eminem (RGB)')
plt.axis('off')
plt.show()

# Optional: Show in OpenCV window
cv2.imshow('Eminem - RGB', img)         # original BGR
# cv2.imshow('Eminem - Grayscale', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional debug print
print("Grayscale Image Matrix:")
print(gray)
