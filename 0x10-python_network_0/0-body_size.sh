#!/bin/bash
# Take in a url, send a reques to the url and display the size of the boddy
# of the response

curl -s "$1" | wc -c
