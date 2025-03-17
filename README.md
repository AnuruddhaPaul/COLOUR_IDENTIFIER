# Color Object Tracker


Color Object Tracker is a computer vision-based system that detects and tracks objects of a specific color using an IP camera feed. This project leverages OpenCV for image processing and PIL for bounding box detection.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview
This project implements a real-time color detection and tracking system. Using a camera feed, you can:

- Detect objects of a specific color (yellow by default)
- Track objects with bounding boxes around the detected color
- Exit the program by pressing the q key

## Requirements
Ensure you have the following installed:

- Python 3.6+
- OpenCV
- NumPy
- PIL (Python Imaging Library/Pillow)
- Access to an IP camera or webcam

## Installation
Clone this repository:

bash
git clone https://github.com/yourusername/color-object-tracker.git
cd color-object-tracker


Install the required dependencies:

bash
pip install opencv-python numpy pillow


## Usage
Run the main script:

bash
python main.py


By default, the program will:

- Connect to the IP camera at the URL specified in the script
- Detect yellow objects in the camera feed
- Draw green bounding boxes around detected objects
- Display coordinates in the console

## Code Explanation

### util.py
This utility file contains a function to calculate HSV color limits for a given BGR color.

#### HSV Color Conversion:
python
def get_limits(colour):
    c = np.uint8([[colour]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

- Converts a BGR color to HSV color space

#### Color Range Definition:
python
lower_Limit = hsv[0][0][0]-10, 100, 100
upper_Limit = hsv[0][0][0]+10, 255, 255

- Creates a range of HSV values centered around the target color
- The range is ±10 in hue, with fixed saturation and value ranges

### main.py
This script contains the main logic for color detection and tracking.

#### Camera Connection:
python
url = 'http://10.5.126.236:8080/video'
cap = cv2.VideoCapture(url)

- Connects to an IP camera using its URL

#### Color Detection:
python
yellow = [0, 255, 255]
hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_Limit, upper_Limit = get_limits(yellow)
mask = cv2.inRange(hsvimage, lower_Limit, upper_Limit)

- Converts each frame to HSV color space
- Creates a binary mask where white pixels represent the detected color

#### Object Tracking:
python
mask_ = Image.fromarray(mask)
bbox = mask_.getbbox()
if bbox is not None:
    xi, y1, x2, y2 = bbox
    frame = cv2.rectangle(frame, (xi, y1), (x2, y2), (0, 255, 0), 2)

- Uses PIL to find the bounding box of detected objects
- Draws a green rectangle around the detected object

## Customization
You can modify the code to suit your needs:

### Change Target Color:
python
# Change this line in main.py to detect a different color
yellow = [0, 255, 255]  # [B, G, R] format

# Examples:
# red = [0, 0, 255]
# green = [0, 255, 0]
# blue = [255, 0, 0]


### Adjust HSV Range Sensitivity:
python
# In util.py, modify these lines:
lower_Limit = hsv[0][0][0]-10, 100, 100  # Change -10 to adjust hue range
upper_Limit = hsv[0][0][0]+10, 255, 255  # Change +10 to adjust hue range


### Use Local Webcam Instead of IP Camera:
python
# Replace the URL line with:
cap = cv2.VideoCapture(0)  # 0 for default webcam


## Troubleshooting

| Issue                | Solution |
|----------------------|----------|
| No camera connection | Check if the IP camera URL is correct |
| Poor color detection | Adjust HSV range values in util.py |
| High CPU usage       | Reduce frame size or processing frequency |
| No objects detected  | Ensure proper lighting and color visibility |
| ImportError          | Verify all dependencies are installed |

## License
This project is licensed under the MIT License.

_Last updated: March 17, 2025_
