import openai
from flask import Flask, render_template, request
import random

openai.api_key = "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"  # Replace with your actual OpenAI API key

app = Flask(__name__)
app.static_folder = 'static'


def chatbot_response(msg):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    # Integrate the user's input with chatbot's response
    chatbot_reply = chatbot_response(user_text)
    return chatbot_reply


if __name__ == "__main__":
    app.run()
