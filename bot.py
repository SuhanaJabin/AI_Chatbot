import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write an essay on flowers"}
    ]
)

message = response['choices'][0]['message']['content']
print(message)
