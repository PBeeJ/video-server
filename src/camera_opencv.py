"""
 This was originally pilfered from
 https://github.com/adeept/Adeept_RaspTank/blob/a6c45e8cc7df620ad8977845eda2b839647d5a83/server/camera_opencv.py

 Which looks like it was in turn pilfered from
 https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited

"Great artists steal". Thank you, @adeept and @miguelgrinberg!
"""

import os
import time
import threading
import datetime
import numpy as np
import cv2

from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        print('initializing VideoCapture')

        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            if img is None:
                if ImgIsNone == 0:
                    print(
                        "The camera has not read data, please check whether the camera can be used normally.")
                    print(
                        "Use the command: 'raspistill -t 1000 -o image.jpg' to check whether the camera can be used correctly.")
                    ImgIsNone = 1
                continue

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
