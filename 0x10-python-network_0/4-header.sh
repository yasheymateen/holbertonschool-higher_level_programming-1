#!/bin/bash
# Sends GET request with a custom Header Variable and displays the body of the response
curl -s $1 -H "X-HolbertonSchool-User-Id: 98"
