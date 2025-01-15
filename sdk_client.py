import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    model="gpt-4o"
)

print(response.choices[0].message.content) 