from flask import Flask, render_template, request
import openai
import asyncio

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = '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'

async def ask_openai_gpt(question):
    response = await asyncio.to_thread(
        openai.Completion.create,
        engine="davinci-002",
        prompt=question,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
async def ask():
    user_input = request.form['user_input']
    response_text = await ask_openai_gpt(user_input)
    return response_text

if __name__ == '__main__':
    app.run(debug=True)
