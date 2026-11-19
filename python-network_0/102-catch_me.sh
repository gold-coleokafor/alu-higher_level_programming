#!/bin/bash
# Makes the server answer with You got me!
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
