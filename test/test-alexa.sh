#!/bin/bash

if [ -z "$1" ]
  then
    URL=http://localhost:5000/games
  else
    URL=$1
fi

HEADER="Content-Type: application/json" \

DATA=`cat alexa.json`
echo $DATA
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/agree"
