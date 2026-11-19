#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
