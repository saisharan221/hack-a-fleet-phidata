import os
from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent
import json

# Load the API key from a .txt file
def get_api_key(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"API key file '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the API key: {e}")

# Path to your .txt file
api_key_path = "api_key.txt"
api_key = get_api_key(api_key_path)

if not api_key:
    raise ValueError("API key is missing. Ensure the .txt file contains the key.")

# Set up the OpenAIChat model with the API key
openai_model = OpenAIChat(model="gpt-4o", api_key=api_key)

# Set up the DuckDbAgent
data_analyst = DuckDbAgent(
    model=openai_model,
    semantic_model=json.dumps({
        "tables": [
            {
                "name": "ferry-trips-data",
                "description": "A CSV file containing records of trips made by 5 ferries owned by Färjerederiet...",
                "path": "ferry_trips_data.csv",
            },
            {
                "name": "ferries-info",
                "description": "A JSON file containing information of the ferries owned by Färjerederiet...",
                "path": "ferries.json",
            },
            {
                "name": "ljusteroleden_oktober_april_schedule",
                "description": "Schedules for the ferry route Ljusteroleden",
                "path": "schedules/ljusteroleden_oktober_april_utg22_2020_w.csv",
            },
            {
                "name": "furusundsleden-blidoleden-schedule",
                "description": "Schedules for the ferry route Furusundsleden, Yxlan ferry",
                "path": "schedules/furusundsleden-blidoleden_utg9_200623_w.csv",
            }
        ]
    }),
    markdown=True,
)

print("Type 'exit' to quit.")
while True:
    user_input = input("Ask your question: ")
    if user_input.lower() == 'exit':
        break
    data_analyst.print_response(user_input, stream=True)
