import ollama

change_text = """
NPCI released a new UPI circular
regarding dispute routing logic.
"""

prompt = f"""
You are a Payments Domain Analyst.

Analyse the update below.

UPDATE:
{change_text}

Provide:

1. Summary
2. Business Impact
3. Priority (High/Medium/Low)
4. Recommended Action
"""

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])