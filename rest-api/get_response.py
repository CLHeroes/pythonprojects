import requests
response_values = requests.get("http://192.168.1.37:5000/ziyotek")
print(response_values.text)