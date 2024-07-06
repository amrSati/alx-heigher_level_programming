#!/bin/bash
# Displays the size of the body of the response of an HTTP request to a given URL

curl -o /dev/null -s -w "%{size_download}\n" "$1"
