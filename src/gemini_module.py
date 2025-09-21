 
import requests
from config.config import GEMINI_API_KEY

def ask_gemini(question):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": question,
        "max_output_tokens": 100
    }
    response = requests.post("https://api.generativeai.google/v1beta2/models/text-bison-001:generate", json=data, headers=headers)
    if response.status_code == 200:
        answer = response.json()["candidates"][0]["content"]
        return answer
    else:
        return "Sorry, I could not get an answer from AI."
