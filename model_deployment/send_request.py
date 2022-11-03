# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:00:41 2022

@author: Anas
"""

## a new customer informations
customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

import requests ## to use the POST method we use a library named requests
url = 'http://localhost:9696/predict' ## this is the route we made for prediction
response = requests.post(url, json=customer) ## post the customer information in json format
result = response.json() ## get the server response
print(result)
