import cv2
import numpy as np

# Function to place image on black regions
def place_image_on_black(image_path, overlay_image_path, output_path):
    '''
    ⁡⁢⁣⁢𝗢𝗻𝗹𝘆 𝗙𝗼𝗿 𝗗𝗲𝘁𝗲𝗰𝘁 𝗕𝗹𝗮𝗰𝗸 𝗖𝗼𝗹𝗼𝗿:⁡
    
    Step 1: load both images
    Step 2: convert image in grayscale which allow detect black color
    Step 3: Now Create a mask where black color convert in white and other convert in full black
    Step 4: detect the contours of the white regions in the mask
    Step 5: used predefine method to get x,y and height and width (y, x: These represent the top-left corner)
    Step 6: Resize the image from height and width (which we get from predefined method)
    Step 7: Now get x and y value where image is overlay (roi = image[y:y+h, x:x+w]), So now ROI is black part where i overlay image
    Step 8: Now Used For loop to place image
    Step 9: Save Image
    '''
    
    # Load the main image
    image = cv2.imread(image_path)
    
    # Load the overlay image
    overlay = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("detect_flow/gray.jpeg",gray)
    
    # Create a mask for black regions (black regions will have pixel values close to 0)
    _, black_mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite("detect_flow/black_mask.jpg",black_mask)
    # Find contours of the black regions
    contours, _ = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through contours and place the overlay image on black regions
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Resize overlay image to match the size of the black region
        resized_overlay = cv2.resize(overlay, (w, h))

        # Get the region of interest (ROI) in the main image
        roi = image[y:y+h, x:x+w]

        # Overlay the resized image onto the ROI
        for i in range(3):  # for each channel (BGR)
            roi[:, :, i] = np.where(resized_overlay[:, :, 3] > 0, resized_overlay[:, :, i], roi[:, :, i])
            
        # Replace the ROI in the image with the modified ROI
        image[y:y+h, x:x+w] = roi

    # Save the resulting image
    cv2.imwrite(output_path, image)

# Example usage
place_image_on_black('try.png', 'doctor.png', 'detect_flow/output_image.jpg')
