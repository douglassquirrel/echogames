#!/bin/bash

if [ -z "$1" ]
  then
    URL=http://localhost:5000/games
  else
    URL=$1
fi

curl -L \
     --header "Content-Type: application/json" \
     --request POST \
     --data '{"request":{"intent":{"slots":{"line": "Star is cute"}}}}' \
     "$URL/agree"

curl -L \
     --header "Content-Type: application/json" \
     --request POST \
     --data '{"request":{"intent":{"slots":{"line": "The moon is purple"}}}}' \
     "$URL/disagree"

curl -L \
     --header "Content-Type: application/json" \
     --request POST \
     --data '{"request":{"intent":{"slots":{"line": "The moon is purple"}}}}' \
     "$URL/doesnotexist"
