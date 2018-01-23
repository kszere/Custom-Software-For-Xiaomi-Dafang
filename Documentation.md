# How use api.cgi?
## Code informations of request.
CODE | Description
------------ | -------------
1234 | In soon ...

## Show data from file and system
### /cgi-bin/api.cgi?action=showlog or /cgi-bin/api.cgi?action=showlog&raw-0
>View data from all /var/log/* file in HTML page.
#### Additional Param
##### raw=1
>View data from all /var/log/* file in RAW text.


## Control System
### /cgi-bin/api.cgi?action=reboot
>Rebooting camera.

Return: 
```json
{
code: 1234,
status: "info",
description: "Rebooting device..."
}
```

### /cgi-bin/api.cgi?action=poweroff
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "info",
description: "Power off camera..."
}
```

### /cgi-bin/api.cgi?action=sethostname&hostname=Dafang
> Set hostname on System.

Return: 
```json
{
code: 1234,
status: "success",
description: "The hostname has been changed successfully to 'Dafang'."
}
```
```json
{
code: 1234,
status: "info",
description: "The hostname is already set to 'Dafang', so has not been changed."
}
```
```json
{
code: 1234,
status: "error",
description: "An error occurred while changing the hostname."
}
```

## Control LED and IR
### /cgi-bin/api.cgi?action=blue_led_on
>Safe power off camera.

Return:
```json
{
code: 1234,
status: "success",
description: "Blue LED is On."
}
```

### /cgi-bin/api.cgi?action=blue_led_off
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "Blue LED is Off."
}
```


### /cgi-bin/api.cgi?action=yellow_led_on
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "Yellow LED is On."
}
```


### /cgi-bin/api.cgi?action=yellow_led_off
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "Yellow LED is Off."
}
```


### /cgi-bin/api.cgi?action=ir_led_on
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "IR LED is On."
}
```


### /cgi-bin/api.cgi?action=ir_led_off
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "IR LED is Off."
}
```


### /cgi-bin/api.cgi?action=ir_cut_on
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "IR cut is On."
}
```


### /cgi-bin/api.cgi?action=ir_cut_off
>Safe power off camera.

Return: 
```json
{
code: 1234,
status: "success",
description: "IR cut is Off."
}
```
## Control Motor PTZ
### /cgi-bin/api.cgi?action=motor_left
>The motor has moved the camera to the left.
### /cgi-bin/api.cgi?action=motor_right
>The motor has moved the camera to the right.
### /cgi-bin/api.cgi?action=motor_up
>The motor has moved the camera to the up.
### /cgi-bin/api.cgi?action=motor_down
>The motor has moved the camera to the down.

Return ex for move left: 
```json
{
code: 1234,
status: "success",
description: "The motor has moved the camera to the left for '100'ms."
}
```
#### Additional Param
##### ns=[value]
>Set value in range 0 - 2500 ns.

Return ex for move right with 600 ns: 
```json
{
code: 1234,
status: "success",
description: "The motor has moved the camera to the right for '600'ms."
}
```

### /cgi-bin/api.cgi?action=motor_vcalibrate
>Motor is calibration on vertical.
### /cgi-bin/api.cgi?action=motorr_hcalibrate
>Motor is calibration on horizontal.
### /cgi-bin/api.cgi?action=motor_calibrate
>Motor is calibration on vertical and horizontal.

## Control Audio
### /cgi-bin/api.cgi?action=audio_test
>Camera playing audio for test.
### /cgi-bin/api.cgi?action=audio_record_start
>Camera start record audio to file.
### /cgi-bin/api.cgi?action=audio_record_stop
>Camera stop record audio to file.

## Control Video
### /cgi-bin/api.cgi?action=h264_start
>Camera start stream video in H264 format.
### /cgi-bin/api.cgi?action=mjpeg_start
>Camera start stream video in MJPEG format.
### /cgi-bin/api.cgi?action=rtsp_stop
>Camera stop stream video in H264 and MJPEG format.

## Other
### /cgi-bin/api.cgi?action=xiaomi_start
>Camera starting with factory firmware.
