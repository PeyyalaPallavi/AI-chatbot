import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(user_input):
    """
    Send user input to OpenAI API and get AI response.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 model
        prompt=user_input,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()
