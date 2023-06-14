import openai
import gradio



messages = [
    {"role": "system", "content": "You are a psychologist."}
]

def CustomChatGPT(user_input, user_role):
    messages.append({"role": user_role, "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply

inputs = [
    gradio.inputs.Textbox(label="User Input"),
    gradio.inputs.Radio(["assistant", "friend", "teacher"], label="User Role")
]

output = gradio.outputs.Textbox(label="ChatGPT Reply")

demo = gradio.Interface(fn=CustomChatGPT, inputs=inputs, outputs=output, title="Digital Psychologist")

demo.launch(share=True)
