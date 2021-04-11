#!/usr/bin/env python3
"""
Handles errors duing message
requests using requests
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error Code: {}".format(response.status_code))
    else:
        print(response.text)
