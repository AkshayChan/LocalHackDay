
# coding: utf-8

# In[6]:


import requests
import json
url = "https://developers.zomato.com/api/v2.1/cuisines"

querystring = {"city_id":"76"}

payload = ""
headers = {
    'Accept': "application/json",
    'user-key': "003f529e396bd67def725a6998d3114b",
    'cache-control': "no-cache",
    'Postman-Token': "4d4bacb5-850b-4bc6-b2d7-eaf0a4763ebb"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
response.json()

