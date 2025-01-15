# GitHubModels

GitHubModels is a Python package that provides strongly typed models for interacting with the GitHub API through Azure OpenAI models. It simplifies the process of making AI-powered GitHub operations by providing a clean, type-safe interface and comprehensive error handling.

## Setup

Install OpenAI SDK using pip (Requires: Python >=3.8):
```bash
pip install openai
```

To use this package, you'll need to set up your GitHub token as an environment variable:

If you're using bash:
```bash
export GITHUB_TOKEN="<your-github-token-goes-here>"
```

If you're using Python:
```python
import os
os.environ['GITHUB_TOKEN'] = '<your-github-token-goes-here>'

# Or in your .env file:
# GITHUB_TOKEN=<your-github-token-goes-here>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.