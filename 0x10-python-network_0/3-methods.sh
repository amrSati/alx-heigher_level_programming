#!/bin/bash
# Displays all HTTP methods of a given URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
