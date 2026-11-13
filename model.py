from ollama import chat

def predict(anchor, text_a, text_b, model="narrative-baseline"):
    prompt = f"""

Anchor Story:
{anchor}

Candidate A:
{text_a}

Candidate B:
{text_b}
"""
    response = chat(
        model=model,
        messages=[{"role":"user", "content":prompt}]
        )

    answer = response.message.content.strip().upper()

    if answer == "A":
        return True
    elif answer == "B":
        return False

    return None