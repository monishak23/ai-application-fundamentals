from google import genai;
from google.genai import types;

client = genai.Client(api_key="")


# System prompt ( persona + rules )
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents="Priya is 25 years old, lives in Bangalore, and works as a software engineer",
    config=types.GenerateContentConfig(
        system_instruction="Consider yourself as a language translator. Rules: Translate everything to French and it should less than 3 sentences.",
    )
)

print(response.text)

# Chain of thoughts ( reasoning for each steps )

# without chain of thoughts
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents="Priya has 2 mangoes, she shared it with her friend one. What will be remaining with her?",
#     config=types.GenerateContentConfig(
#         system_instruction="Solve this",
#     )
# )

# with chain of thoughts
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents="Priya has 2 mangoes, she shared it with her friend one. What will be remaining with her?",
#     config=types.GenerateContentConfig(
#         system_instruction="Before providing the answer provide reason for each step on why and finalise the answer",
#     )
# )

# Few shot classifier
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents=[
#                 # Example 1
#                 {"role": "user", "parts": [{"text": "India won world cup"}]},
#                 {"role": "model", "parts": [{"text": "SPORTS"}]},
#
#                 # Example 2
#                 {"role": "user", "parts": [{"text": "AI trends are emerging"}]},
#                 {"role": "model", "parts": [{"text": "TECH"}]},
#
#                 # Example 3
#                 {"role": "user", "parts": [{"text": "Elections in TN"}]},
#                 {"role": "model", "parts": [{"text": "POLITICS"}]},
#
#                 # Final Instruction
#                 {"role": "user", "parts": [{"text": "Anthropic launched AI plugins"}]}
#             ],
#     config=types.GenerateContentConfig(
#         system_instruction= "Classify each message as exactly one of: TECH, SPORTS, or POLITICS. Reply with only the label, nothing else."
#     )
# )


# JSON extraction
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents= "parse the sentence : Book flight from Mumbai to Delhi on 15th April for 2 people",
#     config=types.GenerateContentConfig(
#         system_instruction= "Parse and print each field",
#         response_mime_type = "application/json"
#     )
# )
