#!/bin/sh

if [ -f /system/sdcard/scripts/func.sh ]; then
  source /system/sdcard/scripts/func.sh
else
  echo "[`date +"%Y-%m-%d %H:%M:%S"`][ERROR] - Functions file 'func.sh' not found."
  exit 1
fi

runWithValid "cp -f /system/sdcard/config/camera.conf /run/camera.conf" "copy 'camera.conf' from microSD to '/run/camera.conf'"

while [ true ]
do
  set -a;source /system/sdcard/config/camera.conf;set +a
#  runWithValid "set -o allexport;source /system/sdcard/config/camera.conf;set +o allexport" "update configuration from 'camera.conf' file"
  sleep 10
done
