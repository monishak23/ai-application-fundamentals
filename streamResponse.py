from google import genai
from google.genai import types

client = genai.Client(api_key="")

todos = []

def add(task: str):
    todos.append(task)

def list_tasks() -> list:
    if not todos:
        return ["No tasks are there"]
    else:
        return todos

chat = client.chats.create(
    model="gemini-2.5-flash-lite",
    config= types.GenerateContentConfig(
        tools = [add,list_tasks],
        system_instruction= "You are a helpful todo assistant. Help me to manage my tasks"
    )
)
for chunk in chat.send_message_stream(
    """Add buy groceries to my list.
    What are my tasks?
    Get code review.
    Drink coffee.
    Show the list of tasks."""):
    print(chunk.text, end="", flush=True)
