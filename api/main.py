import requests # package used to fetch an api



# response coming back is an object that contains information about the response we got back
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response.status_code)

# can have the response raise the exception for us if a bad response comes back
response.raise_for_status() # this method will raise an exception if we have a bad response

data = response.json()
print(data)
