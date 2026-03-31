from google import genai
from google.genai import types


def get_weather(city: str) -> dict:
    """Shows the temperature and humidity for a city"""
    weather_data = {
        "Delhi": {"temp": 28, "condition": "Sunny"},
        "Mumbai": {"temp": 32, "condition": "Humid"},
        "Chennai": {"temp": 35, "condition": "Hot"},
        "Bengaluru": {"temp": 28, "condition": "Sunny"},
    }
    return weather_data.get(city, {"temp": 20, "condition": "Unknown"})

def calculcate(expression: str)  -> float:
    return eval(expression)

def time(city: str) -> dict:
    """Shows the time for a city"""
    data = {"Bengaluru": {"time": "4pm", "state": "Evening"},}
    return data.get(city, {"time": "2pm", "state": "Evening"})

client = genai.Client(api_key="")

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Find the weather of Bengaluru and what is 15% of 50?",
    config = types.GenerateContentConfig(
        tools = [get_weather, calculcate, time]
    )
)

print(response.text)