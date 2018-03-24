#!/bin/sh

if [ -f /system/sdcard/scripts/func.sh ]; then
  source /system/sdcard/scripts/func.sh
else
  echo "[`date +"%Y-%m-%d %H:%M:%S"`][ERROR] - Functions file 'func.cgi' not found."
  exit 1
fi


while true
do

	if [ -z $CONFIG_LDR_AVG ]; then CONFIG_LDR_AVG=1; fi
	# if no config availabe, use 1 as average

	dd if=/dev/jz_adc_aux_0 count=20 | sed -e 's/[^\.]//g' | wc -m >> /run/ldr &>/dev/null
	# add new line to file with measurements

	tail -n $CONFIG_LDR_AVG /run/ldr > /run/ldr_tmp
	mv /run/ldr_tmp  /run/ldr
	# cut /var/run/ldr to desired number of lines

	LINES=`cat /run/ldr | wc -l`
	if [ $LINES -lt $CONFIG_LDR_AVG ]; then CONFIG_LDR_AVG=$LINES; fi
	# to avoid slow switching when starting up, use the number of lines when there are less than the average
	# this may cause some flickering when starting up

	SUM=`awk '{s+=$1} END {printf "%.0f", s}' /run/ldr`
  [[ ! $SUM -eq 0 -o ! $CONFIG_LDR_AVG -eq 0 ]] && AVGMEASUREMENT=$(( $SUM / $CONFIG_LDR_AVG )) || AVGMEASUREMENT=0 # calculate the average

	if [ $AVGMEASUREMENT -lt 50 ]; then # light detected

    if [ $CONFIG_GLOBAL_RENDER_BW -eq 0 -o ! $CONFIG_GLOBAL_RENDER_BW -eq 0 -a ! $CONFIG_GLOBAL_RENDER_BW -eq 1 ]; then
      runWithValid "$BINPATH/setconf -k n -v 0" "switch v4l2rtspserver to day vision"
    elif [ $CONFIG_GLOBAL_RENDER_BW -eq 1 ]; then
      runWithValid "$BINPATH/setconf -k n -v 1" "switch v4l2rtspserver to night vision"
    fi

    if [ $CONFIG_GLOBAL_IR -eq 0 -o ! $CONFIG_GLOBAL_IR -eq 0 -a ! $CONFIG_GLOBAL_IR -eq 1 ]; then
      runWithValid "setGpio 49 1" "changing IR LED to disable"
    elif [ $CONFIG_GLOBAL_IR -eq 1 ]; then
      runWithValid "setGpio 49 0" "changing IR LED to enable"
    fi

    if [ $CONFIG_GLOBAL_IR_CUT -eq 1 -o ! $CONFIG_GLOBAL_IR_CUT -eq 0 -a ! $CONFIG_GLOBAL_IR_CUT -eq 1 ]; then
      runWithValid "setGpio 25 0 && setGpio 26 1" "changing IR CUT to enable"
    elif [ $CONFIG_GLOBAL_IR_CUT -eq 0 ]; then
      runWithValid "setGpio 25 1 && setGpio 26 0" "changing IR CUT to disable"
		fi

	else # nothing in Buffer -> no light

    if [ $CONFIG_GLOBAL_RENDER_BW -eq 1 -o ! $CONFIG_GLOBAL_RENDER_BW -eq 0 -a ! $CONFIG_GLOBAL_RENDER_BW -eq 1 ]; then
      runWithValid "$BINPATH/setconf -k n -v 1" "switch v4l2rtspserver to night vision"
    elif [ $CONFIG_GLOBAL_RENDER_BW -eq 0 ]; then
      runWithValid "$BINPATH/setconf -k n -v 0" "switch v4l2rtspserver to day vision"
    fi

    if [ $CONFIG_GLOBAL_IR -eq 1 -o ! $CONFIG_GLOBAL_IR -eq 0 -a ! $CONFIG_GLOBAL_IR -eq 1 ]; then
      runWithValid "setGpio 49 0" "changing IR LED to enable"
    elif [ $CONFIG_GLOBAL_IR -eq 0 ]; then
      runWithValid "setGpio 49 1" "changing IR LED to disable"
    fi

		if [ $CONFIG_GLOBAL_IR_CUT -eq 0 -o ! $CONFIG_GLOBAL_IR_CUT -eq 0 -a ! $CONFIG_GLOBAL_IR_CUT -eq 1 ]; then
      runWithValid "setGpio 25 1 && setGpio 26 0" "changing IR CUT to disable"
    elif [ $CONFIG_GLOBAL_IR_CUT -eq 1 ]; then
      runWithValid "setGpio 25 0 && setGpio 26 1" "changing IR CUT to enable"
		fi

	fi
  sleep 10
done
