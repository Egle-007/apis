import requests

response = requests.get("http://127.0.0.1:8000/products/5")
print(response.json())