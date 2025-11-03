import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


class GroqClient:   # ✅ Capital G, Capital C
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)

    def get_response(self, message):
        try:
            chat_completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful AI tutor."},
                    {"role": "user", "content": message}
                ]
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error: {str(e)}"
