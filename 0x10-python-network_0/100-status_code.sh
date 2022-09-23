#!/bin/bash
#a Bash script that sends POST to URL
curl -sL -w "%{http_code}" "$1"  -o /dev/null
