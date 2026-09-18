# Smart Image Analysis & Object Detection System

A beginner-friendly image analysis project built using Python and OpenCV.

## Project Overview

This project performs basic image processing and computer vision tasks on an input image. It demonstrates image preprocessing, edge detection, face detection, and basic image analysis.

## Features

- Image loading and validation
- Grayscale image conversion
- Gaussian Blur for noise reduction
- Canny Edge Detection
- Face Detection using Haar Cascade
- Face count detection
- Average image brightness analysis
- Automatic saving of processed images

## Technologies Used

- Python 3.10
- OpenCV
- Haar Cascade Classifier

## Project Structure

```text
Smart_Image_Analysis/
│
├── main.py
├── test.jpg
├── haarcascade_frontalface_default.xml
├── README.md
│
└── output/
    ├── face_detection.jpg
    ├── grayscale.jpg
    ├── blurred.jpg
    └── edges.jpg

How It Works:-
__________________
The input image is loaded using OpenCV.The image is converted into grayscale.Gaussian Blur is applied to reduce image noise.Canny Edge Detection identifies important edges.Haar Cascade is used to detect faces.The number of detected faces is calculated.Average image brightness is calculated.Processed images are saved in the output folder.

Example Result:-

The system successfully detected faces and calculated the average brightness of the input image.

Example:-

Faces detected: 2
Average brightness:68.53

Future Improvements:-
_____________________

1.Object detection

2.Image segmentation

3.Real-time webcam detection

4.Improved face detection

5.Graphical user interface

6.More advanced computer vision techniques

Author:-

GOPISHA PK