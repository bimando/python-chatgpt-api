import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "your-personalized-API-Key"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "",
    "max_tokens": 1000,
    "temperature": 1.7
}


request_data["prompt"] = input("prompt: ")

response = requests.post(api_endpoint, headers=request_headers, json=request_data)


if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    print(response_text)
    with open("output", "w") as file:
        file.write(response_text)
else:
    print("Request failed with status code:", str(response.status_code),
          "\n[+]", response.json()["error"]["message"])
