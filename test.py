import requests
url = "http://localhost:5000/show_data"
response = requests.get(url)
print(response.status_code)
