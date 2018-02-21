#!/bin/sh

################################################
# Created by Krzysztof Szeremeta (KSZERE)      #
# kszere@gmail.com | 2018-01-31 | v.0.0.3 Beta #
################################################

source func.cgi
PATH="/system/bin:/bin:/usr/bin:/sbin:/usr/sbin:/media/mmcblk0p2/data/bin:/media/mmcblk0p2/data/sbin:/media/mmcblk0p2/data/usr/bin"

CONFIGPATH=/system/sdcard/config
BINPATH=/system/sdcard/bin
SDPATH=/system/sdcard

setgpio(){
  GPIOPIN=$1
  echo $2 > /sys/class/gpio/gpio$GPIOPIN/value
}

getreturn(){
echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
echo ""
echo "{
  \"code\": $1,
  \"status\": \"$2\",
  \"description\": \"$3\"
}"
}
#getreturn 123 "sc" "desc"


if [ -n "$F_ns" ]; then
  if [ "$F_ns" -le 2500 -a "$F_ns" -ge 0 ]; then
    F_ns=$F_ns
  else
    F_ns=2500
  fi
else
  F_ns=100
fi



export LD_LIBRARY_PATH=/system/lib
export LD_LIBRARY_PATH=/thirdlib:$LD_LIBRARY_PATH
if [ -n "$F_action" ]; then
  case "$F_action" in
# Show data from file and system
  showlog)
    echo "Content-type: text/html; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
    echo ""
    if [ -n "$F_raw" -a "$F_raw" = 1 ]; then
      tail /var/log/*
    else
      echo "<h1>Contents of all log files</h1>"
      echo "<pre>"
      tail /var/log/*
      echo "</pre>"
    fi
    ;;
# System Request
  reboot)
    getreturn 1234 "info" "Camera will reboot."
    /sbin/reboot
    ;;
  poweroff)
    getreturn 1234 "info" "Camera will safely power off."
    /sbin/poweroff
    ;;
  set_hostname)
    if [ -n "$F_hostname" ]; then
      if [ $(cat $CONFIGPATH/hostname.conf) != "$F_hostname" ]; then
        echo "$F_hostname" > $CONFIGPATH/hostname.conf
        hostname $F_hostname
        if [ $(cat $CONFIGPATH/hostname.conf) = "$F_hostname" ]; then
          getreturn 1234 "success" "The hostname has been changed successfully to '$F_hostname'."
        else
          getreturn 1234 "error" "An error occurred while changing the hostname."
        fi
      else
        getreturn 1234 "info" "The hostname is already set to '$F_hostname', so has not been changed."
      fi
    else
      getreturn 1234 "info" "The \\\"hostname\\\" parameter is empty, so has not been changed."
    fi
    ;;
  set_timezone)
    if [ -n "$F_timez" ]; then
      if [ $(cat /etc/TZ) != "$F_tz" ]; then
        echo "$F_tz" > /etc/TZ
        if [ $(cat /etc/TZ) = "$F_tz" ]; then
          $BINPATH/busybox ntpd -q -n -p time.google.com 2>&1
          getreturn 1234 "success" "The timezone has been changed successfully to '$F_tz'."
        else
          getreturn 1234 "error" "An error occurred while changing the timezone."
        fi
      else
        getreturn 1234 "info" "The timezone is already set to '$F_tz', so has not been changed."
      fi
    else
      getreturn 1234 "info" "The 'tz=[value]' parameter is empty, so has not been changed."
    fi
    ;;
  systeminfo)
    echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
    echo ""

    echo "{
  \"code\": 123,
  \"status\": \"info\",
  \"description\": \"System informations\",
  \"system\": {
    \"hostname\": \"$(cat $CONFIGPATH/hostname.conf)\",
    \"kernel\": \"$($BINPATH/busybox uname -r)\",
    \"uptime\": $(cat /proc/uptime | cut -d. -f1),
    \"cpu_avg\": $(cat /proc/loadavg | cut -d " " -f1),
    \"datetime\": {
      \"date\": \"$(date +'%Y-%m-%d')\",
      \"time\": \"$(date +'%T')\"
    },
    \"network\": {
      \"mac\": \"$(cat /params/config/.product_config | grep MAC | cut -c16-27 | sed 's/\(..\)/\1:/g;s/:$//')\",
      \"router\": {
        \"name\": \"$(iwgetid -r)\",
        \"mac\": \"$(iwgetid -r -a)\",
        \"ip\": \"$(ifconfig wlan0 | grep 'inet addr'| cut -d: -f2 | cut -d' ' -f1)\",
        \"channel\": $(iwgetid -r -c),
        \"freq\": \"$(iwgetid -r -f | cut -de -f1)\",
        \"rx\": $(ifconfig wlan0 | grep 'RX bytes' | cut -d: -f2 | cut -d' ' -f1),
        \"tx\": $(ifconfig wlan0 | grep 'TX bytes' | cut -d: -f3 | cut -d' ' -f1),
        \"signal\": $(cat /proc/net/wireless | tr -s ' ' $'\t' | grep wlan0: | cut -f4 | cut -d. -f1)
      }
    },
    \"disk_space\": {
      \"total\": $(df | tr -s ' ' $'\t' | grep /dev/mmcblk0p1 | cut -f2),
      \"used\": $(df | tr -s ' ' $'\t' | grep /dev/mmcblk0p1 | cut -f3),
      \"free\": $(df | tr -s ' ' $'\t' | grep /dev/mmcblk0p1 | cut -f4)
    },
    \"memory\": {
      \"total\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep MemTotal: | cut -f2),
      \"free\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep MemFree: | cut -f2),
      \"buffers\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep Buffers: | cut -f2),
      \"cached\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep Cached: | cut -f2 | head -1),
      \"swap\": {
        \"total\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep SwapTotal: | cut -f2),
        \"free\": $(cat /proc/meminfo  | tr -s ' ' $'\t' | grep SwapFree: | cut -f2)
      }
    }
  }
}"

    # cpu dane użycia | /proc/stat
    # skanowanie sieci | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:"
    # MAC  | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | tr -s ' ' $'\t' | grep Address: | cut -f6
    # NAME | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | grep ESSID: | cut -d\" -f2
    # FREQ | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | grep Frequency: | cut -d: -f2 | cut -d" " -f1
    # CH   | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | grep Frequency: | cut -d: -f2 | cut -d" " -f4 | cut -d")" -f1
    # SIG  | iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | grep Quality= | cut -d= -f2 | cut -d"/" -f1
    ;;
# Control LED and IR
  blue_led_on)
    setgpio 38 1
    setgpio 39 0
    getreturn 1234 "success" "Blue LED is On."
    ;;
  blue_led_off)
    setgpio 39 1
    getreturn 1234 "success" "Blue LED is Off."
    ;;
  yellow_led_on)
    setgpio 38 0
    setgpio 39 1
    getreturn 1234 "success" "Yellow LED is On."
    ;;
  yellow_led_off)
    setgpio 38 1
    getreturn 1234 "success" "Yellow LED is Off."
    ;;
  ir_led_on)
    setgpio 49 0
    getreturn 1234 "success" "IR LED is On."
    ;;
  ir_led_off)
    setgpio 49 1
    getreturn 1234 "success" "IR LED is Off."
    ;;
  ir_cut_on)
    setgpio 25 1
    setgpio 26 0
    getreturn 1234 "success" "IR cut is On."
    ;;
  ir_cut_off)
    setgpio 25 0
    setgpio 26 1
    getreturn 1234 "success" "IR cut is Off."
    ;;
# Control Motor PTZ
  motor_stop)
    $BINPATH/motor -d s &>/dev/null &
    getreturn 1234 "success" "The motor on the camera has stopped."
    ;;
  motor_left)
    $BINPATH/motor -d l -s $F_ns &>/dev/null &
    getreturn 1234 "success" "The motor has moved the camera to the left for '$F_ns'ms."
    ;;
  motor_right)
    $BINPATH/motor -d r -s $F_ns &>/dev/null &
    getreturn 1234 "success" "The motor has moved the camera to the right for '$F_ns'ms."
    ;;
  motor_up)
    $BINPATH/motor -d u -s $F_ns &>/dev/null &
    getreturn 1234 "success" "The motor has moved the camera to the up for '$F_ns'ms."
    ;;
  motor_down)
    $BINPATH/motor -d d -s $F_ns &>/dev/null &
    getreturn 1234 "success" "The motor has moved the camera to the down for '$F_ns'ms."
    ;;
  motor_calibrate)
     $BINPATH/motor -d v -s 100 &>/dev/null &
     $BINPATH/motor -d h -s 100 &>/dev/null &
     getreturn 1234 "success" "Motor is calibration on vertical and horizontal."
  ;;
  motor_vcalibrate)
     $BINPATH/motor -d v -s 100 &>/dev/null &
     getreturn 1234 "success" "Motor is calibration on vertical."
  ;;
  motor_hcalibrate)
     $BINPATH/motor -d h -s 100 &>/dev/null &
     getreturn 1234 "success" "Motor is calibration on horizontal."
  ;;
# Control Audio
  audio_test)
    $BINPATH/ossplay -g 1000 /usr/share/notify/CN/init_ok.wav &
    getreturn 1234 "info" "Play test audio."
    ;;
  audio_record_start)
    $BINPATH/busybox nohup $BINPATH/ossrecord $SDPATH/test.wav &>/dev/null &
    getreturn 1234 "info" "Audio recording to the \"audio.wav\" file has been started."
  ;;
  audio_record_stop)
    killall ossrecord
    getreturn 1234 "success" "The \"ossrecord\" process was killed."
  ;;
# Control Video
  h264_record_start)
    $BINPATH/busybox nohup $BINPATH/h264Snap > $SDPATH/video.h264 &>/dev/null &
  ;;
  h264_record_stop)
  killall h264Snap
  getreturn 1234 "success" "The \"ossrecord\" process was killed."
  ;;
  h264_start)
    $BINPATH/busybox nohup $BINPATH/v4l2rtspserver-master -F 10 &>/dev/null &
    ;;
  mjpeg_start)
    $BINPATH/busybox nohup $BINPATH/v4l2rtspserver-master -fMJPG -F 10 &>/dev/null &
  ;;
  rtsp_stop)
    killall v4l2rtspserver-master
  ;;
  get_snaphot)
    if [ `ps | grep v4l2rtspserver-master | grep -v grep | wc -l` -eq 1 ]; then
      PARAMS=" -v 0 -rtsp_transport tcp -y -i rtsp://0.0.0.0:8554/unicast -vframes 1"
      if [ -n $F_width -a -n $F_height -a $F_width -eq $F_width -a $F_height -eq $F_height ]; then PARAMS="$PARAMS -s $F_width"x"$F_height"; else PARAMS="$PARAMS -s 640x360"; fi
      if [ $F_flip == 1 ]; then PARAMS="$PARAMS  -vf transpose=1,transpose=1"; fi
      PARAMS="$PARAMS -f image2 /run/snaphot.jpg"

      $BINPATH/busybox nohup $BINPATH/avconv $PARAMS
    else
      export LD_LIBRARY_PATH=/system/lib
      export LD_LIBRARY_PATH=/thirdlib:$LD_LIBRARY_PATH
      PARAMS=""

      if [ $F_nightvision == 1 ]; then PARAMS="$PARAMS -n"; fi
      if [ $F_flip == 1 ]; then PARAMS="$PARAMS -r"; fi
      if [ -n $F_width -a $F_width -eq $F_width ]; then PARAMS="$PARAMS -W $F_width"; else PARAMS="$PARAMS -W 1920"; fi
      if [ -n $F_height -a $F_height -eq $F_height ]; then PARAMS="$PARAMS -H $F_height"; else PARAMS="$PARAMS -H 1080"; fi

      $BINPATH/v4l2rtspserver-master -fMJPG $PARAMS -O /stdout > /run/snaphot.jpg
    fi

    if [ -e /run/snaphot.jpg ]; then
      if [ $F_json == 1 ]; then
        echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
        echo ""
        echo "{
  \"code\": 123,
  \"status\": \"info\",
  \"description\": \"Take a snaphot.\",
  \"snaphot\": \"`cat /run/snaphot.jpg | $BINPATH/busybox base64 | tr -d '\n'`\"
}"
        rm /run/snaphot.jpg
      else
        echo "Content-type: image/jpg; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
        echo ""
        cat /run/snaphot.jpg
        rm /run/snaphot.jpg
      fi
    else
      getreturn 1234 "error" "An error occurred while taking snaphot."
    fi
  ;;
# Other
  check_light)
#    if [ `dd if=/dev/jz_adc_aux_0 count=10 | sed -e 's/[^\.]//g' | wc -m` -lt 30 ]; then
    if [ `dd if=/dev/jz_adc_aux_0 count=20 | sed -e 's/[^\.]//g' | wc -m` -lt 50 ]; then
      getreturn 1234 "info" "Light sensor say's Day"
    else
      getreturn 1234 "info" "Light sensor say's Night"
    fi
  ;;
  xiaomi_start)
    getreturn 1234 "info" "Official software will running."
    busybox insmod /driver/sinfo.ko  2>&1
    busybox rmmod sample_motor  2>&1
    $BINPATH/busybox nohup /system/bin/iCamera &  &>/dev/null &
  ;;
  *)
  getreturn 1234 "error" "Unsupported command '$F_action'"
  ;;
  esac
  fi


exit 0


# START NOTES

# @Crontab
# /system/sdcard/bin/busybox crontab
# /system/sdcard/bin/busybox crond

# @RSTP with Auth
# /system/sdcard/bin/busybox nohup /system/sdcard/bin/v4l2rtspserver-master -fMJPG -U admin:pass &>/dev/null &

# print "Status: 400 Bad Request", "\n\n";

# night_vision_toggle(){
# if [ $( cat /sys/class/gpio/gpio25/value ) -eq "1" ];
#   then
#     setgpio 25 0
#     setgpio 26 1
#     setgpio 49 1
#   else
#     setgpio 25 1
#     setgpio 26 0
#     setgpio 49 0
# fi
# }
