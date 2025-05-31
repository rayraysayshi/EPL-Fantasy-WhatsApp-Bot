# gemini_summarizer.py

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_banter(gw, names, bottom_4):
    team_scores = "\n".join([f"{name}: {score} pts" for name, score in bottom_4])
    prompt = f"Gameweek {gw} has ended. These 4 FPL managers had the worst scores: {names}.\n{team_scores}\n\nWrite a funny, savage British-style recap making fun of their performance."

    # Use a model that supports generateContent from your list
    # For general text, 'gemini-1.5-flash-latest' is a good, fast option.
    # You could also use 'gemini-pro-vision' or 'gemini-1.5-pro-latest'
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

    response = model.generate_content(prompt)

    return response.text