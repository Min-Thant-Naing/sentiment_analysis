import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
API_TOKEN = "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"

if not API_TOKEN:
    print("❌ No API key found. Check your .env file.")
    exit()

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def sentiment_analyzer(text):
    payload = {"inputs": text, "options": {"wait_for_model": True}}
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()          # raises if 4xx/5xx
    return resp.json()  
