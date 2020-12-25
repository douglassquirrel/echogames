#!/bin/bash

if [ -z "$1" ]
  then
    URL=http://localhost:5000/post/
  else
    URL=$1
fi

curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"request":{"intent":{"slots":{"line": "Star is cute"}}}}' \
     $URL
