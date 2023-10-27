import requests

# response = requests.get("http://127.0.0.1:8000/products/all/")
# print(response.json())

response = requests.get("http://127.0.0.1:8000/products/5")
print(response.json())

# response = requests.get("http://127.0.0.1:8000/products/by_category/clothes")
# print(response.json())