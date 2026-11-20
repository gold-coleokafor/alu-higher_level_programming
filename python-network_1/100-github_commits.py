#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
