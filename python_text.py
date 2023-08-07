import requests
import argparse


parser = argparse.ArgumentParser()
# parser.add_argument("prompt", help="the prompt to send to openai API")
# args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

headers={
    "Content-Type": "application/json",
    "Authorization": "Bearer "+ api_key
}

request_data={
    "model": "text-davinci-003",
    "promp": f"write python script to print hello world ",
    "max_token": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=headers, json=request_data)
print(response.json())
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open("output.py", "w") as file:
        file.write(response_text)
else:
    print("request failed with status code: "+str(response.status_code))
