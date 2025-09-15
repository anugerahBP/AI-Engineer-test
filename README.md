# AI-Engineer-test
# Color Detection using OpenCV

## Description
This project detects RED and YELLOW colors in real-time using OpenCV and a webcam.

## Installation
```bash
cd C:\Users\Dzulfikri\AppData\Local\Programs\Python\Python311\Scripts\color-detection-opencv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

How to Run:
python color_detection.py

How it Works

Capture real-time video from webcam.

Convert frame from BGR to HSV.

Apply color range masks for RED and YELLOW.

Display detected color text overlay.
