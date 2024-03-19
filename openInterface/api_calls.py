from openai import OpenAI
from dotenv import load_dotenv
import os

# Set your OpenAI API key
load_dotenv()
api_key = os.getenv("API_KEY")

# Initialize the OpenAI API client
client = OpenAI(api_key=api_key)

def generate_response(prompt):
    """
    Generates a response from the OpenAI API based on the given prompt.

    Args:
        prompt (str): The prompt/query to send to the API.

    Returns:
        str: The API response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None