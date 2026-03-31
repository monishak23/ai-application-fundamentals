from google import genai
from google.genai import types

client = genai.Client(api_key="")

history = []

def chat(msg):

    history.append({
        "role": "user",
        "parts": [{"text": msg}]
    })

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = history
    )

    history.append({
        "role": "model",
        "parts": [{"text": response.text}]
    })

    return history

print(chat("Hello, I am Monisha"))
print(chat("I live Bengaluru"))
print(chat("I am a Software Engineer"))
print(chat("What do you know about me?"))

for turn in history:
    print(turn["role"])
    print(turn["parts"][0]["text"])