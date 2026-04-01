from google import genai
from google.genai import types
from file_reader import read_file

client = genai.Client(api_key="AIzaSyBR3kSjrltpGMnugys9jmiBjmWVkchWg9M")

def create_chats(file):
    doc_text = read_file(file)

    def summarize_document() -> str:
        """Summarize the entire document in 3 bullet points."""
        return doc_text

    def extract_key_info() -> str:
        """Extract key info like names, dates, ages, places from the document."""
        return doc_text

    def length_of_document() -> str:
        """Return the total word count and character count of the document."""
        words = len(doc_text.split())
        chars = len(doc_text)
        return f"{words} words and {chars} characters."

    system_prompt = f"""You are a helpful document assistant.
Answer questions ONLY based on the document below.
If the answer is not found say: "Could not find answer to the above question."
Do not use any outside knowledge. Do not hallucinate.

--- DOCUMENT START ---
{doc_text}
--- DOCUMENT END ---"""

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config= types.GenerateContentConfig(
            system_instruction= system_prompt,
            tools = [summarize_document, extract_key_info, length_of_document],
        )
    )

    return chat


def print_help():
    print("""
    Commands:
      history     — show conversation history
      clear       — start a fresh conversation
      help        — show this menu
      quit        — exit
        """)

def run_chat():
    chats = create_chats("test.txt")

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("Bye Bye")
            break

        if not user_input:
            continue

        if user_input == "quit":
            print("Bye Bye")
            break
        if user_input == "help":
            print_help()
            continue
        if user_input == "history":
            for turn in chats.get_history():
                print(f"{turn.role} : {turn.parts[0].text}")
            continue
        if user_input == "clear":
            chats = create_chats("test.txt")
            print("Conversation cleared")
            continue

        print("Gemini: ", end="", flush=True)
        for chunk in chats.send_message_stream(user_input):
            print(chunk.text, end="", flush=True)  # ← flows smoothly
        print("\n")

run_chat()
