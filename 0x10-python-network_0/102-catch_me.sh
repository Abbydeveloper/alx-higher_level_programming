#!/bin/bash
# Make a server respond with the message 'You got me! in the body of the response
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
