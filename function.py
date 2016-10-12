# -*- coding: utf-8 -*-

import requests

def get_request(url):
    r = requests.get(url)
    return r.status_code

def get_response(url):
    r = requests.get(url):
    return r.content
