import requests

# APIトークンは外部に公開しないこと
API_KEY = "sk-********"

header = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {API_KEY}",
}

body = '''
{
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "こんにちは！"}
    ]
}
'''

response = requests.post("https://api.openai.com/v1/chat/completions", headers = header, data = body.encode('utf_8'))

rj = response.json()
print(rj["choices"][0]["message"]["content"])
