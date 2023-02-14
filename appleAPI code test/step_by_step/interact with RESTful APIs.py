import requests

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
    data = response.json()
    # do something with data
else:
    # handle error response
    error_message = response.text
    # do something with error_message


# I'm making a GET request to the BC Partner API, 
# passing in headers with an access token and query parameters. 
# Then I'm checking the status code of the response to determine 
# whether the request was successful or not, and handling the response accordingly