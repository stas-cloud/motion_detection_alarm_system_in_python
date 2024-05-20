# Motion Detection Alarm System

This project implements a motion detection alarm system using Python and OpenCV on Windows 10. It captures video from the default camera, detects motion in the video stream, and triggers an alarm when motion is detected.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- imutils
- winsound

## Installation

1. **Python Installation**: If Python is not already installed, download and install Python from the [official website](https://www.python.org/downloads/).

2. **OpenCV Installation**: Install OpenCV using pip:
    ```
    pip install opencv-python
    ```

3. **NumPy Installation**: Install NumPy using pip:
    ```
    pip install numpy
    ```

4. **imutils Installation**: Install imutils using pip:
    ```
    pip install imutils
    ```

## Usage

1. Clone the repository or download the `motion_detection_alarm.py` file.

2. Open a command prompt or terminal and navigate to the directory containing `motion_detection_alarm.py`.

3. Run the script:
    ```
    python motion_detection_alarm.py
    ```

4. The camera will start capturing video. Press the 't' key to toggle the alarm mode. Press the 'q' key to quit the program.

## Configuration

- **Camera Selection**: By default, the script uses the default camera. You can change the camera index in the `cv2.VideoCapture()` function call if you have multiple cameras.

- **Motion Sensitivity**: Adjust the sensitivity of motion detection by changing the threshold value in the code.

## camera_test.py

camera_test.py file is for troubleshooting only

run $ python camera_test.py to test whether your camera is working or not.
