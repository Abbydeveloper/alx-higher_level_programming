#!/bin/bash
# Send a JSON POST request to a URL and then display the body of the response
curl -sX POST -H "Content-Type: application/json" -d '${cat "$2"}' "$1"
