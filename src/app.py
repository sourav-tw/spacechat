import gradio as gr
import requests


def chat(question, history):
    url = "http://localhost:5000/api/question"
    data = {"question": question}
    req = requests.session()
    response = req.post(url, json=data, stream=True)
    for line in response.iter_lines():
        if line:
            yield "assistant: " + line.decode("utf-8")


gr.ChatInterface(chat).launch()
