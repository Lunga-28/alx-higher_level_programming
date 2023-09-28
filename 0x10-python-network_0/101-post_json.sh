#!/bin/bash
# send a Json POST and display the response
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
