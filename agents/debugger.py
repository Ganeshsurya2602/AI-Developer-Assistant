from llm import ask_llm

def debug_code(code):
    messages =[
        {"role": "system", 
         "content": "You are a debugging expert. Fix bugs and explain them."},
        
        {"role": "user", 
         "content": f"Fix this code:\n {code}"}
    ]
    return ask_llm(messages)