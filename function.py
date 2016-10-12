# -*- coding: utf-8 -*-

import requests

def get_request(url):
    # request for url to get status_code
    r = requests.get(url)
    return r.status_code

def get_response(url):
    r = requests.get(url):
    return r.content
