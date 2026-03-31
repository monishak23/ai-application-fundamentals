from google import genai
from google.genai import types

client = genai.Client(api_key="")

def chat_bot():

    chat = client.chats.create(
        model="gemini-2.5-flash-lite",
    )

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nBye!")
            break

        if user_input == "quit":
            break
        if user_input == "history":
            for turn in chat.get_history():
                print(turn.role)
                print(turn.parts[0].text)
                print("----------------------------------")
            continue
        print("Final chunk------------")
        for chunk in chat.send_message_stream(user_input):
            print(chunk.text, end="", flush=True)

chat_bot()