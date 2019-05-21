import cv2
import numpy as np

# get video capture
video_capture = cv2.VideoCapture(0)

# get frame
def get_frame():

    if cv2.waitKey(1) & 0xFF == ord('q'):
        video_capture.release()
        cv2.destroyAllWindows()
        return None

    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    cv2.imshow('Video', small_frame)
    return rgb_small_frame
