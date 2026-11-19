#!/bin/bash
# Displays the size in bytes of the response body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
