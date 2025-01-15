# GitHubModels

A Python package demonstrating different methods of interacting with Azure OpenAI models through both the OpenAI SDK and REST API.

## Features

- SDK-based implementation using the OpenAI Python package
- REST API implementation using the requests library
- Support for Azure OpenAI endpoints
- Environment variable configuration

## Setup

Install required packages using pip (Requires: Python >=3.8):
```bash
pip install openai requests
```

To use this package, you'll need to set up your API token as an environment variable:

If you're using bash:
```bash
export GITHUB_TOKEN="<your-api-token-goes-here>"
```

If you're using Python:
```python
import os
os.environ['GITHUB_TOKEN'] = '<your-api-token-goes-here>'

# Or in your .env file:
# GITHUB_TOKEN=<your-api-token-goes-here>
```

## Usage

### Using the OpenAI SDK

```python
from chat import client

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Your question here",
        }
    ],
    model="gpt-4o"
)
```

### Using REST API

```python
from rest import headers, url

data = {
    "messages": [{"role": "user", "content": "Your question here"}],
    "model": "gpt-4o"
}
response = requests.post(url, headers=headers, json=data)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.