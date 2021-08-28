
#/bin/sh
# this script is meant to be run from your local development machine.


if [ "$1" == "" ]; then
  echo "Error: missing parameter.  usage: sbin/upload.sh user@IP_ADDRESS_OR_NAME"
  exit 1
fi

set -x

TARGET_DIR="/home/pi/video-server"
TARGET_HOST=$1
TMP_DIR="/tmp/video-server"

ssh $TARGET_HOST "mkdir -p $TARGET_DIR"

scp -r * $TARGET_HOST:$TARGET_DIR
