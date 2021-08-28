"""
 This was originally pilfered from
 https://github.com/adeept/Adeept_RaspTank/blob/a6c45e8cc7df620ad8977845eda2b839647d5a83/server/camera_opencv.py

"Great artists steal". Thank you, @adeept!
"""

import os
import threading
import datetime
import numpy as np
import cv2

from base_camera import BaseCamera

CVRun = 1
lineColorSet = 255
frameRender = 1
findLineError = 20

ImgIsNone = 0

colorUpper = np.array([44, 255, 255])
colorLower = np.array([24, 100, 100])


class CVThread(threading.Thread):
    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self, *args, **kwargs):
        self.CVThreading = 0
        self.CVMode = 'none'
        self.imgCV = None

        self.radius = 0
        self.box_x = None
        self.box_y = None
        self.drawing = 0

        self.findColorDetection = 0

        super(CVThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.clear()

    def mode(self, invar, imgInput):
        self.CVMode = invar
        self.imgCV = imgInput
        self.resume()

    def elementDraw(self, imgInput):
        if self.CVMode == 'none':
            pass

        elif self.CVMode == 'findColor':
            if self.findColorDetection:
                cv2.putText(imgInput, 'Target Detected', (40, 60),
                            CVThread.font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                self.drawing = 1
            else:
                cv2.putText(imgInput, 'Target Detecting', (40, 60),
                            CVThread.font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                self.drawing = 0

            if self.radius > 10 and self.drawing:
                cv2.rectangle(imgInput, (int(self.box_x-self.radius), int(self.box_y+self.radius)),
                              (int(self.box_x+self.radius), int(self.box_y-self.radius)), (255, 255, 255), 1)

        return imgInput

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def run(self):
        while 1:
            self.__flag.wait()
            if self.CVMode == 'none':
                continue
            elif self.CVMode == 'findColor':
                self.CVThreading = 1
                self.findColor(self.imgCV)
                self.CVThreading = 0
            pass


class Camera(BaseCamera):
    video_source = 0
    modeSelect = 'none'
    # modeSelect = 'findlineCV'
    # modeSelect = 'findColor'
    # modeSelect = 'watchDog'

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

        cvt = CVThread()
        cvt.start()

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

            if Camera.modeSelect == 'none':
                cvt.pause()
            else:
                if cvt.CVThreading:
                    pass
                else:
                    cvt.mode(Camera.modeSelect, img)
                    cvt.resume()
                try:
                    img = cvt.elementDraw(img)
                except:
                    pass

            # encode as a jpeg image and return it
            if cv2.imencode('.jpg', img)[0]:
                yield cv2.imencode('.jpg', img)[1].tobytes()
