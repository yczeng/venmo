'''
Balance module.
'''
import logging
import json
import requests
import venmo

logger = logging.getLogger('venmo.payment')

def balance():
    access_token = venmo.auth.get_access_token() 
    if not access_token: 
        logger.warn('No access token. Configuring ...') 
        if not venmo.auth.configure(): 
            return 
        access_token = venmo.auth.get_access_token() 

    response = requests.get('https://api.venmo.com/v1/me?access_token=' + access_token)
    response_dict = response.json()
    print(response_dict['data']['balance'])
    return response_dict['data']['balance']