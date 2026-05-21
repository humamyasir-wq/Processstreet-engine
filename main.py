import requests

API_KEY = "ضع_api_key_هنا"

url = "https://api.process.st/templates"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "name": "AML Workflow"
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)
