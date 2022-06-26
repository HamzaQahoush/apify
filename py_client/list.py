from email import header
from wsgiref import headers
import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"  # http://127.0.0.1:8000/

password = getpass()
auth_response = requests.post(
    auth_endpoint, json={"username": "hamza", "password": password}
)  # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8000/api/products/"
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Token {token}"}
    get_reponse = requests.get(endpoint, headers=headers)
    print(get_reponse.json())
