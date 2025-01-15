import base64, requests, os

try:
    with open("sample.jpg", "rb") as f:
        b64_image = base64.b64encode(f.read()).decode('utf-8')
except Exception as e:
    print(f"Image error: {e}")
    exit()

try:
    response = requests.post(
        "https://models.inference.ai.azure.com/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}"},
        json={"model": "gpt-4o", "messages": [{"role": "user", "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}", "detail": "low"}}
        ]}]}
    )
    print(response.json()["choices"][0]["message"]["content"])
except Exception as e:
    print(f"API error: {e}\nStatus: {response.status_code}\nResponse: {response.text}")