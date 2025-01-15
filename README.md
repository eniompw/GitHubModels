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

### Using the OpenAI SDK (sdk_client.py)

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

### Using REST API (rest.py)

```python
import requests
import os

url = "https://models.inference.ai.azure.com/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("GITHUB_TOKEN"))}
data = {"messages": [{"role": "user", "content": "Your question here"}], "model": "gpt-4o"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
```

### Image Analysis (images.py)

The package also supports image analysis using GPT-4o's vision capabilities. You can provide either a local image path or an image URL:

```python
# Example usage:
python images.py
# When prompted, enter either:
# - A local file path (e.g., "images/photo.jpg")
# - An image URL (e.g., "https://example.com/image.jpg")
```

The script will analyze the image and provide a description of its contents.

## Project Structure

- `sdk_client.py`: OpenAI SDK implementation
- `rest.py`: REST API implementation
- `images.py`: Image analysis implementation using the REST API

## References

For more information about the GPT-4o model and its capabilities, see the [Azure OpenAI GPT-4o Marketplace listing](https://github.com/marketplace/models/azure-openai/gpt-4o).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.