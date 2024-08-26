#!/bin/bash
#display all HTTP methods a server withh accept
curl -SI 0.0.0.0:5000/route_4 | grep 'Allow' | cut -d ' ' -f 2-
