#!/bin/sh

# This script is meant to be run on the bot.  The upload.sh script in
# this directory will upload us and all of ./sbin to $TARGET_DIR
#
# This setup copied from here: https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition


set -x

TARGET_DIR="/home/pi/video-server"
TMP_DIR="/tmp/video-server"

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y \
git \
python3-pip

###
#
# These I needed to install to use open cv on the
# raspian lite (no desktop gui)
#
sudo apt-get install -y \
python3-h5py \
libharfbuzz-dev \
libwebp-dev \
libtiff-dev \
libilmbase23 \
libopenexr-dev \
libgstreamer1.0-dev \
libavcodec-dev \
libavformat-dev \
libswscale-dev \
libqtgui4 \
libqt4-test

###
#
#  Added for Adeept video streaming; see,
#  base_camera.py, comaner_opencv.py + other code originally
#  sourced from @adeept/Adeept_RaspTank.
#
#  Thank you @adeept!  ❤️ you!

# I added these to accomodate adeept video streaming
sudo apt-get install -y libjasper-dev
sudo apt-get install -y libatlas-base-dev

# These are for the webserver (flask) and websocket server
sudo pip3 install websockets flask flask_cors
# I'm not sure why Caroline's cv2 setup didn't work for adeept.
# I originally tried to leave this out
sudo pip3 install opencv-contrib-python==3.4.3.18

sudo pip3 install zmq pybase64


##
# End Adeept setup
##