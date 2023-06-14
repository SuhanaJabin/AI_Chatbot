import os
import openai
import gradio

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

openai.api_key = api_key

messages = [
    {"role": "system", "content": "You are a psychologist."}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chatGPT_reply})

    return chatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Digital Psychologist")

demo.launch(share=True)
