from llm import ask_llm

def generate_code(prompt):
    messages =[
        {"role": "system", 
         "content": "You are a proffessional software engineer. Generte code for the given prompt."},
        
        {"role": "user", 
         "content":prompt}
    ]
    return ask_llm(messages)
