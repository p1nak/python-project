# --- JARVIS LOGIC (from jarvis.py) ---
import webbrowser
import wikipedia
import pywhatkit
import requests
import ollama

def process_command(command):
    command = command.lower()

    if command.startswith("open "):
        site = command.split()[1]
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        return f"Opening {site}.com"

    elif "time" in command:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        
    elif command.startswith("play "):
        song = command.replace("play", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube."

    elif "samachar" in command:
        try:
            r = requests.get("https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=YOUR_API_KEY")
            if r.status_code == 200:
                articles = r.json().get('articles', [])
                return " | ".join([article['title'] for article in articles[:5]])
            else:
                return "Sorry, I couldn't fetch the news."
        except Exception as e:
            return "News fetch error."

    elif command.startswith("search"):
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching for {query} on Google."

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=2)
            return result
        except Exception:
            return f"Couldn't find '{topic}' on Wikipedia."

    elif "exit" in command or "stop" in command:
        return "Goodbye!"

    else:
        try:
            response = ollama.chat(
                model="mistral",
                messages=[{"role": "user", "content": command}]
            )
            return response['message']['content']
        except Exception:
            return "Jarvis couldn't process that right now."