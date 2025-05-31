# fpl_bot.py

import requests
from datetime import datetime
from config import LEAGUE_ID
import gemini_summarizer 

def get_latest_gameweek():
    events = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()["events"]
    finished = [e for e in events if e["finished"]]
    return finished[-1]["id"] if finished else None

def get_league_standings(league_id):
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    standings = requests.get(url).json()["standings"]["results"]
    return standings

def get_manager_week_score(entry_id, gw):
    url = f"https://fantasy.premierleague.com/api/entry/{entry_id}/history/"
    history = requests.get(url).json()
    gw_data = history["current"]
    for week in gw_data:
        if week["event"] == gw:
            return week["points"]
    return None

def get_bottom_performers():
    gw = get_latest_gameweek()
    if not gw:
        return None, None

    standings = get_league_standings(LEAGUE_ID)
    scores = []
    for manager in standings:
        name = manager["entry_name"]
        entry_id = manager["entry"]
        gw_score = get_manager_week_score(entry_id, gw)
        scores.append((name, gw_score))

    scores = sorted(scores, key=lambda x: x[1])[:4]
    return scores, gw

def generate_summary():
    bottom_4, gw = get_bottom_performers()
    if not bottom_4:
        return None

    names = ", ".join([b[0] for b in bottom_4])
    return gemini_summarizer.generate_banter(gw, names, bottom_4)

# Added for direct execution
if __name__ == "__main__":
    from whatsapp_sender import send_message_via_whatsapp

    print("Generating FPL summary...")
    summary_message = generate_summary()
    if summary_message:
        print("Summary generated:")
        print(summary_message)
        print("\nSending message to WhatsApp...")
        send_message_via_whatsapp(summary_message)
        print("Message sent!")
    else:
        print("Could not generate summary. Check FPL data or API keys.")