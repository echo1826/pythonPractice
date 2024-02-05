import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "secretshhhhhhh",
    "username": "echo1108",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params) # json is put into the req.body of the request
response.raise_for_status()
print(response.text)