import os
import matplotlib.pyplot as plt
import cv2

image_files = [f for f in os.listdir() if f.endswith('.png')]

for img_file in image_files:
    img = cv2.imread(img_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB (for proper display in matplotlib)

    plt.imshow(img)
    plt.title(img_file)
    plt.axis('off')
    plt.show()

print("Loaded and displayed all PNG images successfully!")
