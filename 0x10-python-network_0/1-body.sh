#!/bin/bash
# Displays the body of the response of a GET request
if [ "$(curl -o /dev/null -s -w "%{http_code}\n" "$1")" -eq "200" ]; then curl "$1"; fi
