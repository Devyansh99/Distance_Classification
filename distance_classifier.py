import os
import matplotlib.pyplot as plt
import cv2

# Check for PNG & JPG image files
image_extensions = [".png", ".jpg", ".jpeg"]
image_files = [f for f in os.listdir() if any(f.endswith(ext) for ext in image_extensions)]

if image_files:
    print(f"Found {len(image_files)} image(s): {image_files}")
    
    for img_file in image_files:
        try:
            img = cv2.imread(img_file)
            if img is None:
                print(f"Warning: Could not load '{img_file}'. Skipping...")
                continue

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display

            plt.imshow(img)
            plt.title(img_file)
            plt.axis("off")
            plt.show()

        except Exception as e:
            print(f"Error loading '{img_file}': {e}")

    print("Successfully loaded and displayed all valid images.")
else:
    print("No image files found in the directory.")

print("Image verification completed.")
