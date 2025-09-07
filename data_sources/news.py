import requests
from datetime import datetime
import os

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(query, from_date, to_date):
    url = f"{BASE_URL}?q={query}&from={from_date}&to={to_date}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}
