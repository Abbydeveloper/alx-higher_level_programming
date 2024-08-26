#!/bin/bash
#display all HTTP methods a server withh accept
curl -s -i -L -X OPTIONS "$1"
