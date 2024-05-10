import threading  # Importing threading module for running beep_alarm function in a separate thread
import winsound   # Importing winsound module for generating beep sound
import cv2        # Importing OpenCV library for computer vision tasks
import imutils    # Importing imutils library for image processing
import numpy as np # Importing numpy library for numerical operations

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Initializing the video capture object with the default camera
                                           # Specify a different index (e.g., 1, 2) if using a different camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)    # Setting the frame width of the captured video stream
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)   # Setting the frame height of the captured video stream

_, start_frame = cap.read()                # Capturing the initial frame from the camera
start_frame = imutils.resize(start_frame, width=500)  # Resizing the frame to a width of 500 pixels
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)  # Converting the frame to grayscale
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)      # Applying Gaussian blur to the grayscale frame

alarm = False          # Variable to track whether the alarm is triggered
alarm_mode = False     # Variable to indicate whether the alarm mode is activated
alarm_counter = 0      # Counter for managing alarm triggering frequency

def beep_alarm():      # Function to generate beeping sound for the alarm
    global alarm
    while alarm_mode:  # Continuously check if the alarm mode is active
        print("ALARM") # Print message indicating alarm activation
        winsound.Beep(2500, 1000)  # Generate a beep sound with frequency 2500 Hz and duration 1000 ms

while True:            # Infinite loop for video streaming and processing
    _, frame = cap.read()  # Capture a frame from the video stream
    frame = imutils.resize(frame, width=500)  # Resize the frame to a width of 500 pixels

    if alarm_mode:    # Check if the alarm mode is active
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)    # Apply Gaussian blur to the grayscale frame

        difference = cv2.absdiff(start_frame, frame_bw)    # Compute absolute difference between frames
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]  # Thresholding to detect motion
        start_frame = frame_bw  # Update the reference frame

        if threshold.sum() > 10000:  # Check if the motion detected exceeds a certain threshold
            alarm_counter += 1       # Increment the alarm counter
            if alarm_counter > 20:   # If motion persists for a certain duration
                if not alarm:       # If alarm is not already triggered
                    alarm = True   # Set alarm flag to True
                    threading.Thread(target=beep_alarm).start()  # Start the beep_alarm function in a separate thread
        else:
            if alarm_counter > 0:  # If no motion detected, decrement the alarm counter
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)  # Display the thresholded image with motion highlighted
    elif not alarm_mode and alarm:   # If alarm mode is deactivated and alarm is triggered
        black_frame = np.zeros_like(frame)  # Create a black frame
        cv2.imshow("Cam", black_frame)      # Display the black frame
    else:
        cv2.imshow("Cam", frame)   # Display the original frame if neither alarm mode nor alarm is triggered

    key_pressed = cv2.waitKey(30)  # Wait for a key press for 30 milliseconds
    if key_pressed == ord('t'):    # If 't' key is pressed
        print("You have activated/deactivated the alarm!")  # Print message indicating alarm mode toggling
        alarm_mode = not alarm_mode  # Toggle the alarm mode
        alarm_counter = 0            # Reset the alarm counter
    elif key_pressed == ord('q'):   # If 'q' key is pressed
        print("Quitting the program!")  # Print message indicating program termination
        alarm_mode = False          # Deactivate alarm mode
        break                       # Exit the loop

cap.release()       # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
