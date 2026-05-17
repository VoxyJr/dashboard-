import requests
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()

def get_weather(city="siavonga"):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text.strip()

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    return f"{data[0]['q']} — {data[0]['a']}"

def get_date():
    return datetime.now().strftime("%A, %B %d %Y  %H:%M")

def main():
    console.print(Panel(get_date(), title="Today", border_style="cyan"))
    console.print(Panel(get_weather("siavonga"), title="Weather", border_style="yellow"))
    console.print(Panel(get_quote(), title="Quote of the Day", border_style="magenta"))

main()
