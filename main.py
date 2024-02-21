import google.generativeai as genai
import os

apikey = os.environ.get('GENAI_API_KEY', '')

genai.configure(api_key=apikey)

model = genai.GenerativeModel('gemini-pro')

print("Using Text Generative AI Model...")

chat = model.start_chat(history=[])

while True:
    prompt = input("\nEnter a prompt (Leave Empty to Exit) : ")

    if prompt == "":
        break

    res = chat.send_message(prompt)

    print(f"\nGemini: {res.text}")
