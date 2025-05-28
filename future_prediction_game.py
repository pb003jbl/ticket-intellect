import os
import random
import requests
import time
from dotenv import load_dotenv

load_dotenv()


def get_mistral_prediction(prompt):
    """
    Calls the Mistral LLM API for a chat completion based on the user's prompt.
    Requires the environment variable MISTRAL_API_KEY to be set.
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Warning: MISTRAL_API_KEY not set. Using random prediction.")
        return random.choice([
            "You will have a lucky day!",
            "A surprise is waiting for you soon.",
            "Be cautious with your decisions today.",
            "An old friend will contact you.",
            "You will achieve something great this week!"
        ])
    try:
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-tiny",  # You can change to another model if needed
            "messages": [
                {"role": "system", "content": "You are a fun and mysterious fortune teller."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 64
        }
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Mistral API error: {e}. Using random prediction.")
        return random.choice([
            "You will have a lucky day!",
            "A surprise is waiting for you soon.",
            "Be cautious with your decisions today.",
            "An old friend will contact you.",
            "You will achieve something great this week!"
        ])

def future_prediction_game():
    print("Welcome to the Future Prediction Game!")
    name = input("Enter your name: ")
    question = input("Ask a question about your future: ")
    print("\nConsulting Mistral AI for your prediction...")
    time.sleep(2)
    prediction = get_mistral_prediction(question)
    print(f"\n{name}, here is your prediction: {prediction}")

if __name__ == "__main__":
    future_prediction_game()
