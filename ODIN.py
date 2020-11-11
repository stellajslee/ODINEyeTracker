"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import serial

arduinoData = serial.Serial('/dev/cu.usbmodem143101', 9600)

from project3.GazeTracking.gaze_tracking.gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(1)

cap = cv2.VideoCapture(1) 
while(1):
    ret, frame = cap.read()
    # cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    # frame = gaze.annotated_frame()
    text = ""

    # if gaze.is_blinking():
        # text = "Blinking"
    if gaze.is_right():
        text = "Looking right"
        arduinoData.write(b'1')
        
    elif gaze.is_left():
        text = "Looking left"
        arduinoData.write(b'0')
        
    elif gaze.is_center():
        text = "Looking center"
            
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (45, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (45, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
    
    
