#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status using the package requests"""
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
