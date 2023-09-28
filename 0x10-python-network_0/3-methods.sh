#!/bin/bash
# displays all HTTP methods that server accepts
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
