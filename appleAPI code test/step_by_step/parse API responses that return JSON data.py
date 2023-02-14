import requests
import json   

# must have API key 
url = "https://api.example.com/partner"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <your_access_token>"
}
params = {
    "param1": "value1",
    "param2": "value2"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    # handle successful response
    data = json.loads(response.text)
    # do something with data (e.g. access specific fields)
    print(data["field1"])
else:
    # handle error response
    error_message = response.text
    # do something with error_message

# I'm still making a GET request to the BC Partner API and checking the status code of the response. 
# However, this time 
# I'm using the json.loads() method to parse the JSON data returned by the API into a Python dictionary.
# Then I access specific fields within the response using the keys of the dictionary.