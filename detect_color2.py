import cv2
import numpy as np

"""sumary_line

    Step 1: load both images
    Step 2: convert image HSV (HSV is typically preferred over BGR for color-based detection tasks)
     - define lower bound and upper bound when mix both bound we get green color
    Step 3: Now Create a mask where black color convert in white and other convert in full black
    Step 4: detect the contours of the white regions in the mask
    Step 5: used predefine method to get x,y and height and width (y, x: These represent the top-left corner)
    Step 6: Resize the image from height and width (which we get from predefined method)
    Step 7: Now get x and y value where image is overlay (roi = image[y:y+h, x:x+w]), So now ROI is black part where i overlay image
    Step 8: Now Used For loop to place image
    Step 9: Save Image

"""



# Load the main image and overlay image
image_path = 'Assets/try2.png'  # Replace with the path to your main image
overlay_image_path = 'Assets/doctor.png'  # Replace with the path to your overlay image
image = cv2.imread(image_path)
overlay = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

# Convert the main image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the green color range in HSV
lower_green = np.array([35, 40, 40])   # Lower bound of green
upper_green = np.array([85, 255, 255]) # Upper bound of green

# Create a mask for green regions
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Find contours of the green regions
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over each green region found
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    # Resize the overlay image to fit the green region
    resized_overlay = cv2.resize(overlay, (w, h))

    # Get the region of interest (ROI) in the main image
    roi = image[y:y+h, x:x+w]

    # Overlay the resized image onto the ROI, taking transparency into account
    for i in range(3):  # For each channel (BGR)
        roi[:, :, i] = np.where(resized_overlay[:, :, 3] > 0, resized_overlay[:, :, i], roi[:, :, i])

    # Replace the ROI in the image with the modified ROI
    image[y:y+h, x:x+w] = roi

# Save the final output
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)
