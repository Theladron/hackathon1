# & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/PhilW/PycharmProjects/Hackathon/Wiki_title.py
# 12.35
import random
import data_handling
import user_input


def create_player_dict():
    player_number = user_input.get_number_of_players()

    players = {}

    # Spielerinfos sammel und Dictionary erstellen
    for player in range(player_number):
        player_name = user_input.get_player_name(player)
        # Füge Spieler zum Dict mit Score 0 als Start
        players[f"Player{player + 1}"] = {"name": player_name, "score": 0}

    return players


# Funktion, um einen zufälligen Artikel auszuwählen
def get_random_article():
    """
    Wählt zufällig einen Artikel aus der vordefinierten Kategorie-Liste aus.
    """
    categories = {
        "Germany", "Albert_Einstein", "Python", "Physics",
        "Second_World_War", "Literature", "Artificial_Intelligence", "Space_Travel"
    }

    # Wähle zufällig ein Titel
    title = random.choice(list(categories))
    return title


# Funktion, um den Text des Artikels zu holen
def get_section_text(article):
    """
    Holt den Abschnitt des Artikels und gibt ihn zurück.
    """
    try:
        text = data_handling.get_page_summary(article)

        # Ersetze den Titel durch "_"
        modified_text = text.replace(article, "_" * len(article))
        return modified_text 
    except data_handling.exceptions.DisambiguationError as e:
        return f"There was an error in the article search"
    except data_handling.exceptions.HTTPTimeoutError:
        return "Timeout occurred while fetching the page."
    except data_handling.exceptions.RedirectError:
        return "The page was redirected."


# Hauptspiel-Funktion
def game(player):
    """
    Hauptspiel-Funktion: Der Spieler muss den Titel des Artikels erraten.
    """
    print("-------------------------------------")
    print("--- Welcome to the WikiTitle Game ---")
    print("-------------------------------------")
    print()
    print("Task explanation")
    print("You have to guess the title of the section!")
    print()

    for player_key, current_player in player.items():
        score = current_player["score"]
        article = get_random_article()
        section_text = get_section_text(article)

        print(f"Player {current_player['name']}, read the following paragraph and try to guess the title:")
        print()
        print(section_text)

        # Benutzerantwort
        answer = input("\nWhat do you think is the title of the article? ")

        # Eingabe prüfen
        new_article = article.replace("_"," ")
        if answer.lower() == new_article.lower():
            print(f"Correct! The title was: {new_article}")
            score += 1
        else:
            print(f"Unfortunately wrong. The correct title was: {new_article}")

        # Aktualisiere den Punktestand des Spielers
        current_player["score"] = score
        print(f"Current score of {current_player['name']}: {current_player['score']}")
        print("Next Player! Your Turn :)")

    # Anzeige Endergebnis
    print("Game Over!")
    for player_key, current_player in player.items():
        print(f"{current_player['name']} final score: {current_player['score']}")



if __name__ == "__main__":
    players = create_player_dict()
    print("Players Dictionary:", players)
    game(players)
    