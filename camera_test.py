import cv2
import imutils

# Initialize VideoCapture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read the first frame
_, start_frame = cap.read()

# Check if the frame is read successfully
if start_frame is None:
    print("Error: Unable to read frame from camera.")
    exit()

# Resize, convert to grayscale, and apply Gaussian blur to the start frame
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# Continue with your motion detection code...
