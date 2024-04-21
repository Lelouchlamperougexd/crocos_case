from config import GOOGLE_API_G as GOOGLE_API_KEY
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_text(prompt:str):
    prompt = prompt.lower()
    context = open("info.txt", encoding="UTF-8").read().lower()
    prompt = prompt + "\n" + context
    response = model.generate_content(prompt)
    return response.text
