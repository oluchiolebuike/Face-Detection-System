## FACE DETECTION SYSTEM (OPEN-CV)


## Overview

This project is a simple real-time face detection system built using Python and OpenCV.

It detects human faces in images or live webcam feed and draws bounding boxes around them. The system does not identify or recognise individuals — it only detects the presence and location of faces in a frame.

This project is designed for learning computer vision fundamentals and real-time image processing.



## Features

- Real-time face detection using webcam
- Image-based face detection support (optional extension)
- Bounding box overlay on detected faces
- Lightweight OpenCV-based implementation
- No facial recognition or identity tracking



## Technologies Used

- Python
- OpenCV (cv2)
- Haar Cascade Classifier (pre-trained model)



## Installation


1. Install Python dependencies:

pip install opencv-python



## Project Structure


face-detection/
|
|-- face_detection.py
|-- README.txt



## How to Run


### STEP 1: Run the program

python face_detection.py



### STEP 2: Webcam opens automatically

- The system will access your camera
- Detected faces will be highlighted with rectangles



### STEP 3: Exit program

Press "Q" on your keyboard to close the application.


## How It Works


1. The webcam captures live video frames
2. Each frame is converted to grayscale
3. Haar Cascade classifier detects facial regions
4. Bounding boxes are drawn around detected faces
5. Output is displayed in real time



## Limitations


- Works best in good lighting conditions
- May struggle with extreme angles or occlusions
- Does not perform facial recognition or identity matching



## Future Improvements


- Add facial landmark detection (eyes, nose, mouth)
- Integrate deep learning-based detector (CNN / DNN)
- Add face tracking across frames
- Add emotion detection (happy, sad, neutral)
- Improve accuracy using modern models like MediaPipe or RetinaFace



## License

This project is for educational purposes only.
