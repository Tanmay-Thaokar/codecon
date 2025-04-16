import openai
def explain_text_plain_english(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Explain the following legal language in plain English."},
            {"role": "user", "content": text}
        ],
        max_tokens=600
    )
    return response['choices'][0]['message']['content']
