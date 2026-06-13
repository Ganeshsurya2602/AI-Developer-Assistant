import os

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def ask_llm(message):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = message
    )
    return response.choices[0].message.content