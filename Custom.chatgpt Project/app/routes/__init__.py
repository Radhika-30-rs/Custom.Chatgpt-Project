from flask import Blueprint, render_template, request, jsonify
from app.api_client import GroqClient


routes = Blueprint('routes', __name__)

@routes.route('/')
def chat_page():
    return render_template('chat.html')

@routes.route('/api/chat', methods=['POST'])
def chat_api():
    user_input = request.json.get('message', '')
    reply = f"You said: {user_input}"  # Replace with your model response
    return jsonify({"reply": reply})


