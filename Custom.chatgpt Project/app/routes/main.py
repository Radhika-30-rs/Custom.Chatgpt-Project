from flask import Blueprint, render_template, request, jsonify
from app.api_client import GroqClient

main = Blueprint('main', __name__)
groq_client = GroqClient()

@main.route('/')
def index():
    return render_template('chat.html')

@main.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message.strip():
        return jsonify({"response": "Please enter a message."})

    response = groq_client.get_response(message)
    return jsonify({"response": response})



