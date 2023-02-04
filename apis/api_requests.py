# API

# Application Programming Interface
# How software can communicate with one another (they work across different software)

import requests

import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb") (.get just gets everything)
#
# print(post_codes_req) # <Response [200]>
#
# print(post_codes_req.status_code) # 200 (mark that says that it is working)
#
# print(post_codes_req.headers)  # gives us  Raw http headers
#
# print(post_codes_req.content) # gives raw data/content
#
# print(post_codes_req.json()) # json content
#
# print(type(post_codes_req.json())) # <class 'dict'>


json_body = json.dumps({"postcodes": ["PR8 OSG", "M45 6GN", "EX165BL"]}) #set the data that we want to send to api
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body) # we dont need the xtra bit becuase we are specifying

print(post_multi_req.json())





