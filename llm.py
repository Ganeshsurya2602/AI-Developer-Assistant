from groq import Groq

client = Groq(api_key="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")
def ask_llm(message):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = message
    )
    return response.choices[0].message.content

#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