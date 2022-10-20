# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:25:08 2022

@author: Mc
"""

import requests

URL = "https://dog.ceo/api/breeds/image/random"

result = requests.get(URL)

data = result.json()

print(data)



