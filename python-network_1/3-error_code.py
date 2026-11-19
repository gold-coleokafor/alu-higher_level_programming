#!/usr/bin/python3
"""Displays a response body, or the code on an HTTPError."""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
