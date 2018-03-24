#!/bin/sh

if [ -f /system/sdcard/config/camera.conf ]; then
  source /system/sdcard/config/camera.conf
else
  getReturn 123 "error" "Configuration file 'camera.conf' not found."
  exit 1
fi

# START FUNCTIONS
setGpio(){
  echo $2 > /sys/class/gpio/gpio$1/value
  if [ $( cat /sys/class/gpio/gpio$1/value ) -eq "$2" ]; then
    true
  else
    false
  fi
}
# setGpio 49 0

getReturn(){
echo "Content-type: application/json; charset=utf-8; Pragma: no-cache; Expires: Wednesday, 27-Dec-95 05:29:10 GMT"
echo ""
echo "{
  \"code\": $1,
  \"status\": \"$2\",
  \"description\": \"$3\"
}"
}
# getReturn 123 "sc" "desc"

returnLog(){
  if [ $1 == "s" ]; then
    echo -e "\e[1;97m[\e[0m`date +"%Y-%m-%d %H:%M:%S"`\e[1;97m][\e[1;32mSUCCESS\e[1;97m]\e[1;39m - $2\e[0m"
  elif [ $1 == "i" ]; then
    echo -e "\e[1;97m[\e[0m`date +"%Y-%m-%d %H:%M:%S"`\e[1;97m][\e[1;33mINFO\e[1;97m]\e[1;39m - $2\e[0m"
  elif [ $1 == "e" ]; then
    echo -e "\e[1;97m[\e[0m`date +"%Y-%m-%d %H:%M:%S"`\e[1;97m][\e[1;31mERROR\e[1;97m]\e[1;39m - $2\e[0m"
  fi
}
# returnLog "s" "Log data"

runWithValid(){
  $1
  if ! [ $? -eq 0 ]; then
    returnLog "e" "An error occurred while $2."
    exit 1
  fi
}
# runWithValid "command" "return second text"

killAll(){
  ps | grep "$1" | awk '{print $1}' | xargs kill
}
# END FUNCTIONS

# Source: http://isquared.nl/blog/2008/11/01/Bourne-Bash-Shell-CGI-Scripts/

_DEBUG_=

if [ "${REQUEST_METHOD}" = "POST" ]
then
  POST_QUERY_STRING=`dd bs=1 count=${CONTENT_LENGTH} 2>/dev/null`
  if [ "${QUERY_STRING}" != "" ]
  then
      QUERY_STRING=${POST_QUERY_STRING}"&"${QUERY_STRING}
  else
      QUERY_STRING=${POST_QUERY_STRING}"&"
  fi
fi

#echo "Content-type: text/plain"; echo

_IFS=${IFS}; IFS=\&
i=0
for _VAR in ${QUERY_STRING}
do
  if [ ${_DEBUG_} ]
  then
      i=`expr $i + 1`; echo "--- ENTER LOOP $i ---"
      echo _VAR: ${_VAR}
      echo -n variable: `echo ${_VAR} | cut -d= -f1`" "
      echo value: `echo ${_VAR} | cut -d= -f2`
  fi

  eval "`echo F_${_VAR} | cut -d= -f1`=`echo ${_VAR} | cut -d= -f2`"

  if [ ${_DEBUG_} ]
  then
      echo "--- EXIT LOOP $i ---"
  fi
done
IFS=${_IFS}
unset i _IFS _VAR

if [ ${_DEBUG_} ]
then
  echo query string: ${QUERY_STRING}
  echo post-part of query string: ${POST_QUERY_STRING}
fi
