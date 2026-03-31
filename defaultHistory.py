from google import genai
from google.genai import types

client = genai.Client(api_key='')

chat = client.chats.create(
    model="gemini-2.5-flash-lite",
)

chat.send_message("Hello, I am Monisha")
chat.send_message("I live Bengaluru")
chat.send_message("I am a Software Engineer")

for turn in chat.get_history():
    print(turn.role)
    print(turn.parts[0].text)