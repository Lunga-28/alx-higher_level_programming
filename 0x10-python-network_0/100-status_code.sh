#!/bin/bash
# gets status code of response
curl -s "$1" -o /dev/null -w "%{http_code}"
