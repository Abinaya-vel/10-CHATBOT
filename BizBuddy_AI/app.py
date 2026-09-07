import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

client = genai.Client(api_key=API_KEY) if API_KEY else None

SYSTEM_PROMPT = """You are BizBuddy AI, a helpful AI assistant.
Purpose: Business and entrepreneurship assistant.
Give clear, practical, beginner-friendly answers.
Do not claim to be a human or professional.
For high-risk topics, encourage the user to consult a qualified professional.
"""

@app.route("/")
def home():
    return render_template("index.html", bot_name="BizBuddy AI")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message."}), 400

    if not client:
        return jsonify({"reply": "GEMINI_API_KEY is missing. Add it to your .env file."}), 500

    try:
        prompt = SYSTEM_PROMPT + "\n\nUser: " + message
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return jsonify({"reply": response.text or "Sorry, I could not generate a response."})
    except Exception as e:
        return jsonify({"reply": f"Something went wrong: {e}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
