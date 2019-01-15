#!/bin/bash
# Sends a POST request to the passed URL with custom variables, and displays the body of the response.
curl -X POST -s $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
