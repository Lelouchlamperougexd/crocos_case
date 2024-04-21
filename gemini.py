from config import GOOGLE_API_G as GOOGLE_API_KEY
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

prompt = "Расскажи мне что такое city pass"
context = open("info.txt", encoding="UTF-8").read()
prompt = prompt + "\n" + context
response = model.generate_content(prompt)

print(response.text)
