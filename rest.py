import requests
import os

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("GITHUB_TOKEN"))}
query = "What is the capital of France?"
data = {"messages": [{"role": "user", "content": query}], "model": "gpt-4o"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])