from flask import Flask, render_template, jsonify
import requests
import os

OPENAI_API_KEY = os.environ['OPEN_API_KEY']

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index(name=None):
  return render_template('index.html', name=name)


@app.route('/call_api/<prompt>', methods=['GET'])
def call_api(prompt):
  chatHistory = [{"role": "user", "content": prompt}]
  print("CHAT HISTORY", chatHistory)

  resp = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
      "Authorization": "Bearer " + OPENAI_API_KEY,
      "Content-Type": "application/json"
    },
    json={
      "max_tokens": 256,
      "top_p": 1,
      "presence_penalty": 0,
      "frequency_penalty": 0,

      "temperature": 1.0,
      "model": "gpt-3.5-turbo",
      "messages": chatHistory,
    }
  )
  print("sent request to openai")
  print(resp.content)
  resp.raise_for_status()
  response = resp.json()
  print("response from openai: ", response)

  # get actual text from response:
  text = response['choices'][0]['message']['content']
  return jsonify({ text: text })

app.run(host='0.0.0.0', port=81)
