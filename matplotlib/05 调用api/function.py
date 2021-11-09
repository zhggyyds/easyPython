import requests


def get_response_dict(url,headers=None):
    if headers != None:
        r = requests.get(url,headers)
    else:
        r = requests.get(url,headers)
    return r.json()

def get_response_status(url,headers=None):
    if headers != None:
        r = requests.get(url,headers)
    else:
        r = requests.get(url,headers)
    return r