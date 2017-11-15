'''
Balance module.
'''
import json

import requests

import venmo

def balance():
    access_token = venmo.auth.get_access_token()
    response = requests.get('https://api.venmo.com/v1/me?access_token=' + access_token)
    response_dict = response.json()
    print(response_dict['data']['balance'])
    return response_dict['data']['balance']