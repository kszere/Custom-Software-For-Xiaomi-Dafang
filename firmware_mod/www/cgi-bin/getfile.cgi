#!/bin/sh

################################################
# Created by Krzysztof Szeremeta (KSZERE)      #
# kszere@gmail.com | 2018-01-31 |  v0.0.5 Beta #
################################################

# START IMPORT FILES
if [ -f /system/sdcard/scripts/func.sh ]; then
  source /system/sdcard/scripts/func.sh
else
  echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
  echo ""
  echo "
{
  \"code\": 1234,
  \"status\": \"info\",
  \"description\": \"Functions file 'func.cgi' not found.\"
}
"
  exit 1
fi

# END IMPORT FILES

export LD_LIBRARY_PATH=/system/lib
export LD_LIBRARY_PATH=/thirdlib:$LD_LIBRARY_PATH


if [ -n "$F_path" ]; then
  FILEPATH=$(echo $F_path | sed 's/\DCIM\///g' | sed 's/ /\\ /g')

  FILENAME=$($BINPATH/busybox basename $FILEPATH)
  FILEPATH="/system/sdcard/DCIM/$FILEPATH"
  FILESIZE=$(ls -1l "$FILEPATH" | tr -s ' ' $'\t' | cut -f3)
  if [ -f $FILEPATH ]; then
    echo "Content-Location: $FILEPATH
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="$FILENAME"
Content-Transfer-Encoding: binary
Content-Length: $FILESIZE
Pragma: private
Cache-Control: private, must-revalidate
Title: "$FILENAME"
Expires: Thu, 1 Jan 1970 00:00:00 GMT"
    echo ""
    cat $FILEPATH
  else
    getReturn 1234 "error" "File '$FILEPATH' not found."
  fi
else
  getReturn 1234 "info" "Param 'path=[value]' is empty."
fi

exit 0

# http://192.168.44.142/cgi-bin/getfile.cgi?path=DCIM/VideoRecorder/2018-03-06_13.36.mov
