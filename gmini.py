import os
import google.generativeai as genai

API_KEY ="AIzaSyAmDTsDckgD1mOncPqFOqZX8d2wxg5HCoU"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash"))
chat = model.start_chat(history=[])

response = chat.send_message("Hello")
print("Gemini:" , response.text)





