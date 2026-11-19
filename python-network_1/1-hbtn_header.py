#!/usr/bin/python3
"""Displays the X-Request-Id header of a URL's response."""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get("X-Request-Id"))
