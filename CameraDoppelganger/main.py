import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat

# Open the video file
video_path = 'video.mp4'  # Replace with your MP4 file path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Video Resolution: {width}x{height}, FPS: {fps}")

# Open a virtual camera
with pyvirtualcam.Camera(width=width, height=height, fps=int(fps), fmt=PixelFormat.BGR) as cam:
    print(f"Virtual camera started: {cam.device}")

    while True:
        ret, frame = cap.read()
        if not ret:
            # print("End of video or cannot read frame.")
            # break
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame
            continue

        # Optionally, process the frame (e.g., resize, add effects, etc.)
        # For example, converting to grayscale:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Send the frame to the virtual camera
        cam.send(frame)

        # Wait for the next frame
        cam.sleep_until_next_frame()

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            print("Exit key pressed. Stopping...")
            break

# Release the video file
cap.release()
print("Video streaming to virtual camera completed.")
