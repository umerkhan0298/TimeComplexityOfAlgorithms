import requests
import json

url = "https://a605-2406-d00-cccf-7fd1-30f1-f42e-91c7-1b7b.ngrok-free.app"

data = {'inputString': 100000, 'findingElement': 10, 'Linear Search': True, 'Binary Search': True, 'Jump Search': True, 'Ternary Search': True}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.text)
