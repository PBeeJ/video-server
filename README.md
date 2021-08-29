<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [video-server](#video-server)
  - [Getting Started](#getting-started)
      - [Install Raspian OS on SSD card.](#install-raspian-os-on-ssd-card)
      - [Configure PI for Headless](#configure-pi-for-headless)
    - [Run raspi-config](#run-raspi-config)
    - [Upload video-server files to pi](#upload-video-server-files-to-pi)
    - [Run setup.sh on the raspberry pi](#run-setupsh-on-the-raspberry-pi)
    - [Run the server](#run-the-server)
    - [Open the web app](#open-the-web-app)
    - [View FPS stats](#view-fps-stats)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# video-server

This is just the video streaming server. Originally stolen from https://github.com/adeept/Adeept_RaspTank/blob/a6c45e8cc7df620ad8977845eda2b839647d5a83/server/FPV.py

We've added links to the original code in the headers of relevant files.

## Getting Started

#### Install Raspian OS on SSD card.

This setup was tested with Raspian-lite (no desktop GUI)

#### Configure PI for Headless

Follow the instructions here for setting up wifi and ssh:
https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing

### Run raspi-config

Once you are able to connect to the Raspberry Pi via SSH, you should run

```
sudo raspi-config
```

Under "System Options", you may want to select each of the following:

- Password - to change the pi user password, the default is well known
- Hostname - to change the hostname from `raspberrypi.local`

Press escape to return to the main menu.

Under "Interface Options", ** you must enable the following **:

- Camera

Exit raspi-config and `sudo reboot`

### Upload video-server files to pi

If you cloned this project from github to a desktop or laptop, you can run:

```
./upload.sh pi@raspberrypi.local
```

to upload the files.

You can also clone this directly onto the pi

```
cd ~
sudo apt-get install git
git clone https://github.com/PBeeJ/video-server.git
```

### Run setup.sh on the raspberry pi

Via ssh shell into the Raspberry Pi,

```
cd ~/video-server
./setup.sh
```

This will install all of the dependencies like opencv

### Run the server

```
cd ~/video-server
./run.sh
```

### Open the web app

point a browser tab at:

```
http://raspberrypi.local:5000
```

### View FPS stats

point a browser tab at:

```
http://raspberrypi.local:5000/stats
```
