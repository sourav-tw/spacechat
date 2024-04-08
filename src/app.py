import gradio as gr
import requests


def chat(question, history):
    url = "http://localhost:5000/api/question"
    data = {"question": question}
    req = requests.session()
    response = req.post(url, json=data, stream=True)
    assistant_response = "assistant: "
    for line in response.iter_lines():
        if line:
            assistant_response += line.decode("utf-8") + "\n"
            yield assistant_response
    history.append((question, assistant_response))


gr.ChatInterface(chat).launch()
