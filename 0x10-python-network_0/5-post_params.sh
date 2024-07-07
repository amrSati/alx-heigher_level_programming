#!/bin/bash
# Sends a POST request to a given URL with some data
curl -s -d '{"email":"test@gmail.com", "subject:"I will always be here for PLD"}' -X POST "$1"
