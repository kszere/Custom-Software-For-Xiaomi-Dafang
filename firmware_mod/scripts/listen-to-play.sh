#!/bin/sh

if [ -f /system/sdcard/config/camera.conf ]; then
  source /system/sdcard/config/camera.conf
else
  echo "[`date +"%Y-%m-%d %H:%M:%S"`][ERROR] - Configuration file 'camera.conf' not found."
  exit 1
fi

if [ -f $SDPATH/www/cgi-bin/func.cgi ]; then
  source $SDPATH/www/cgi-bin/func.cgi
else
  echo "[`date +"%Y-%m-%d %H:%M:%S"`][ERROR] - Functions file 'func.cgi' not found."
  exit 1
fi

$BINPATH/busybox mkfifo /run/listen-to-play.fifo
if ! [ $? -eq 0 ]; then
  returnLog "e" "An error occurred while create FIFO file."
  exit 1
fi


$BINPATH/ossplay -g $CONFIG_GLOBAL_SPEAKER_GAIN /run/listen-to-play.fifo
