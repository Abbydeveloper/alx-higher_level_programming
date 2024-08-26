#!/bin/bash
#display all HTTP methods a server withh accept
curl -SI "$1" | grep 'Allow' | cut -d ' ' -f 2-
