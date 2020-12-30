#!/bin/bash

if [ -z "$1" ]
  then
    URL=http://localhost:5000/games
  else
    URL=$1
fi

HEADER="Content-Type: application/json" \
DATA_FMT='{"client": "API", "sessionId": "test.session.24244", "line": "%s"}'

printf -v DATA "$DATA_FMT" "Star is cute"
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/agree"

printf -v DATA "$DATA_FMT" "The moon is purple"
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/disagree"

printf -v DATA "$DATA_FMT" "Star is cute"
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/echo"

printf -v DATA "$DATA_FMT" "5"
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/guess"

printf -v DATA "$DATA_FMT" "Star is cute"
curl -L --header "$HEADER" --request POST --data "$DATA" "$URL/doesnotexist"
