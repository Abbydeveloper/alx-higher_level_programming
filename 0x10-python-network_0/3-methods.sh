#!/bin/bash
#display all HTTP methods a server withh accept
curl -s -i -I -X OPTIONS "$1"
