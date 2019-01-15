#!/bin/bash
# Displays only the status code of the HTTP response without using pipes.
curl -s -o /dev/null -w "%{http_code}" $1
