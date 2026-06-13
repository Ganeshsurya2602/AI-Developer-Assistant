from llm import ask_llm

def explain_code(code):
    
    messages =[
        {"role": "system", 
         "content": "Explain code in simple steps."},

        {"role": "user", 
         "content": f"Explain this code:\n {code}"}
    ]
    return ask_llm(messages)