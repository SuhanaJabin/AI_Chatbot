import openai


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is meant by click fraud zombie?"}
    ]
)

message = response['choices'][0]['message']['content']
print(message)
