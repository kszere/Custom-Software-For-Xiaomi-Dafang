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


echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
echo ""
# echo "{
#   \"name\": \"DCIM\",
#   \"type\": \"folder\",
#   \"path\": \"DCIM\",
#   \"items\": [
#     {
#       \"name\": \"Snaphots\",
#       \"type\": \"folder\",
#       \"path\": \"DCIM/Snaphots\",
#       \"items\": []
#     },
#     {
#       \"name\": \"SoundRecorder\",
#       \"type\": \"folder\",
#       \"path\": \"DCIM/SoundRecorder\",
#       \"items\": []
#     },
#     {
#       \"name\": \"VideoRecorder\",
#       \"type\": \"folder\",
#       \"path\": \"DCIM/VideoRecorder\",
#       \"items\": [
#         {
#           \"name\": \"2018-03-06_13.36.mov\",
#           \"type\": \"file\",
#           \"path\": \"DCIM/VideoRecorder/2018-03-06_13.36.mov\",
#           \"size\": 40351122
#         }
#       ]
#     }
#   ]
# }
# "

#jq -n "{items: [\"$ARR\"]}"

#DUMP_DCIM=$(ls -l /system/sdcard/DCIM/)
#ls -lhe /system/sdcard/DCIM/ | tr -s ' ' $'\t' | cut -f11


DCIMPATH="/system/sdcard/DCIM"


exit 0
