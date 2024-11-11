import cv2

# Open the video file
cap = cv2.VideoCapture('video.mp4')

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    frame_count = 0
    while True:
        # Read the next frame
        ret, frame = cap.read()
        
        # If the frame is read correctly, ret is True
        if not ret:
            break

        # Save the frame as an image (optional)
        cv2.imwrite(f'frames/frame_{frame_count}.jpg', frame)
        frame_count += 1

print("Frame Extraction Is Done!")
