#!/bin/bash
# Sends a given JSON file POST request to a given URL
curl -s "$1" -X POST -d "@$2"
