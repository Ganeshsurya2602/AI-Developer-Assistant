from agents.generator import generate_code
from agents.debugger import debug_code
from agents.explainer import explain_code

def router_task(prompt):
    if "fix" in prompt.lower() or "error" in prompt.lower():
        return debug_code(prompt)
    elif "explain" in prompt.lower() and "code" in prompt.lower():
        return explain_code(prompt)
    else:
        return generate_code(prompt)