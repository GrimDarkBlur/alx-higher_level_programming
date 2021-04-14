#!/bin/bash
# prints the content length of a header
# of a get requests using curl

curl -Il "$1" 2>&1|grep content-length -i| cut -d' ' -f2

