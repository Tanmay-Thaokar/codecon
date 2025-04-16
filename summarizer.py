import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text_openai(text, model="gpt-4"):
    if len(text) > 8000:
        text = text[:8000]  # Truncate for token limit
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a legal assistant. Summarize the following legal text."},
            {"role": "user", "content": text}
        ],
        max_tokens=600
    )
    return response['choices'][0]['message']['content']
