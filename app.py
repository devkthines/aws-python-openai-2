from flask import Flask, render_template, request, jsonify
import os
import openai
import asyncio
import threading

app = Flask(__name__)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if openai_api_key is None:
    print("Error: OPENAI_API_KEY environment variable not set.")
else:
    print(f"API Key: {openai_api_key}")

# Now you can use openai_api_key in your OpenAI API calls
def get_openai_response(messages):
    response =  openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message['content']

def run_asyncio_loop(loop, messages):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_openai_response(messages))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    messages = [
        {"role": "system", "content": "You joke around a lot."},
        {"role": "user", "content": user_message}
    ]
    response =  get_openai_response(messages)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)