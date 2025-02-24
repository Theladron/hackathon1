# & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/PhilW/PycharmProjects/Hackathon/WikiTitle Game.py"

import data_handling
import random


players = {
    "Player1": {"name": "Hans", "score": 2},
    "Player2": {"name": "Peter", "score": 2}
}


def get_random_article():
    """
    Wählt zufällig einen Artikel aus der vordefinierten Kategorie-Liste aus.
    """
    categories = {
        "Germany", "Albert_Einstein", "Python_(programming language)", "Physics", 
        "Second_World_War", "Literature", "Artificial_Intelligence", "Space_Travel"
    }

    # Wähle zufällig ein Titel
    title = random.choice(categories)
    return title


def get_section_text(article):
    """
    Holt den Abschnitt des Artikels und zurück.
    """
    try:
        text = data_handling.get_page_summary(article)
        return text
    except data_handling.exceptions.DisambiguationError:
        return "There was an error in the article search"
    

def game(player):
    """
    Hauptspiel-Funktion: Der Spieler muss den Titel des Artikels erraten.
    """
    print("--- Welcome to the WikiTitle Game ---")
    print("You have to guess the titel of the section!")
    for player_key, player in players.item():
        score = 0
        # Hole zufälligen Artikel
        article = get_random_article()
        # Hole Abschnitt des Artikels
        section_text = get_section_text(article)

        print(f"Player {player["name"]}, read the following paragraph and try to guess the title:")
        print(section_text)

        # Benutzerantwort
        answer = input("\nWhat do you think is the title of the article? ")

        # Eingabe prüfen
        if answer.lower() == article.lower():
            print(f"Correct! The title was: {article}")
            score += 1
        else:
            print(f"Unfortunately wrong. The correct title was: {article}")

    player['score'] += score
    print(f"Current score or {player["name"]}: {player["score"]}")
    return player

    # Anzeige Endergebnis
    print("Game Over!")
    for player_key,player in players.items():
        print(f"{player["name"]} final score : {player["score"]}")


if __name__ == "__main__":
    game() 
