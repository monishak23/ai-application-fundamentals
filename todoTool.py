from google import genai
from google.genai import types
from google.genai.chats import Chat

client = genai.Client(api_key="")

todos = []

def add(task: str):
    """Adds a task to the list"""
    todos.append(task)
    return todos

def list_tasks() -> list:
    """Lists all the tasks"""
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
print(chat.send_message("""Add buy groceries to my list.
    What are my tasks?
Get code review.Drink coffee.
Show the list of tasks.""").text)
