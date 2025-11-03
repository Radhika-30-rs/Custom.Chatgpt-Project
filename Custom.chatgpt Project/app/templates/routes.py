# app/routes.py
from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('chat.html')

@main.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simple AI response (replace later with your model)
    if not user_message:
        return jsonify({"response": "⚠️ Please type something!"})

    response_text = f"You said: {user_message}. I'm learning to be smarter 🤖"
    return jsonify({"response": response_text})
