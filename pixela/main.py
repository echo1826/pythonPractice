import requests

USERNAME = "echo1108"
TOKEN = "secretshhhhhhh"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params) # json is put into the req.body of the request
# print(response.status_code)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "days",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) # how to send request headers in a fetch
print(response.text)