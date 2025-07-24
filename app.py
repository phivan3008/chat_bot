import os
import openai
from flask import Flask, request, render_template
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

client = openai.OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL")
)

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = client.chat.completions.create(
            model="GPT-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_response = response.choices[0].message.content
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
