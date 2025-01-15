# GitHubModels

A Python package demonstrating different methods of interacting with Azure OpenAI models through both the OpenAI SDK and REST API.

## Setup

1. Install dependencies:
```bash
pip install openai requests
```

2. Set your API token:
```bash
export GITHUB_TOKEN="<your-api-token-goes-here>"
```

## Usage

### Using the OpenAI SDK

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Your question here"}],
    model="gpt-4o"
)

print(response.choices[0].message.content)
```

### Using REST API

```python
import requests
import os

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("GITHUB_TOKEN"))}
data = {"messages": [{"role": "user", "content": "Your question here"}], "model": "gpt-4o"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
```

## References

For more information about the GPT-4o model and its capabilities, see the [Azure OpenAI GPT-4o Marketplace listing](https://github.com/marketplace/models/azure-openai/gpt-4o).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.