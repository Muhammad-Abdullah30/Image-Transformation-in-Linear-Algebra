import cv2
import numpy as n
import matplotlib.pyplot as p

image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Define the dilation factor
kernel = n.ones((3, 3), n.uint8)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

x_range = n.arange(0, image.shape[1])
y_range = n.arange(0, image.shape[0])

# Displaying the original and dilated images using matplotlib in Cartesian plane
p.figure(figsize=(10, 6))

# Original Image
p.subplot(1, 2, 1)
p.imshow(image, cmap=None, extent=[0, image.shape[1], image.shape[0], 0])
p.title('Original Image')
p.xlabel('X')
p.ylabel('Y')

# Dilated Image
p.subplot(1, 2, 2)
p.imshow(dilated_image, cmap=None , extent=[0, dilated_image.shape[1], dilated_image.shape[0], 0])
p.title('Dilated Image')
p.xlabel('X')
p.ylabel('Y')

p.tight_layout()
p.show()