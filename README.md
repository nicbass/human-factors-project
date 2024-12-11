# Drowsiness Detection

Welcome to our Drowsiness Video Detection Software. The purpose of this project is to help keep drivers safe and awake on the road.

Our system analyzes video through a camera (must have camera) and detects if a user is displaying signs of drowsiness. If so, it responds by sending out an audio and haptic alarm until it detects that they are no longer showing these signs (controller and speaker not provided).

## How to Install and Run

### Installation
1. Install [YOLOv8](https://universe.roboflow.com/drowsy-detection/drowsiness-detection-g3r3l) and download the necessary datasets from this site (Yolov8).
2. Place the downloaded models and datasets in the **main directory** of this project.
3. The program should then be able to be ran through either an IDE of choice or by executing the file "person_detection.py".

### Running the Application
To run the application, use the following command (in the IDE of your choice):
python person_detection.py
