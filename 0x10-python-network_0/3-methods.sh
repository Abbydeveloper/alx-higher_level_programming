#!/bin/bash
#display all HTTP methods a server withh accept
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f 2-
