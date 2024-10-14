from openai import OpenAI
client = OpenAI(
    base_url='https://api.moonshot.cn/v1',
    api_key='sk-bYyvQmVrGmW4tZ61TGDfRxZVVoeHozROaZF4UGGGjcwixcra'
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "你是谁啊",
        }
    ],
    model="moonshot-v1-8k",
)
result = chat_completion.choices[0].message.content
print(result)