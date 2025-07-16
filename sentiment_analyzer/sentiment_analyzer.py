import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
API_TOKEN = os.getenv("HF_API_KEY")

if not API_TOKEN:
    print("❌ No API key found. Check your .env file.")
    exit()

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def sentiment_analyzer(text_to_analyse):
    payload = {"inputs": text_to_analyse, "options": {"wait_for_model": True}}
    r = requests.post(API_URL, headers=headers, json=payload, timeout=5)
    r.raise_for_status()                         # Raise an error for bad responses
    return r.json()[0][0] 