#   & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/PhilW/PycharmProjects/Hackathon/Wiki_title.py

import random
import data_handling
import user_input
import wikipedia

# Funktion, um den Text des Artikels zu holen
def get_section_text(article, word_lst):
    """
    Holt den Abschnitt des Artikels und gibt ihn zurück.
    """
    try:
        text = data_handling.get_page_summary(article)
        new_lst = []
        for word in word_lst:
            new_lst.append(word)
            new_lst.append(word.upper())
            new_lst.append(word.capitalize())
        for word in new_lst:
            # Ersetze den Titel durch "_"
            text = text.replace(word, "_" * len(word))
        return text
    except data_handling.exceptions.DisambiguationError:
        return f"⚠️ There was an error in the article search"
    except data_handling.exceptions.HTTPTimeoutError:
        return "⏳ Timeout: occurred while fetching the page."
    except data_handling.exceptions.RedirectError:
        return "🔄 The page was redirected."


# Funktion checkt die User Eingabe
def check_user_answer(answer_user, word_lst):

    if answer_user.lower() in word_lst[0]:
        return True
    else:
        return False


# Funktion zum speichern der Article in Liste
def check_title_in_article(article):
    word_lst = []

    article = article.replace("(", "")
    article = article.replace(")", "")
    word_lst = article.lower().split()

    return word_lst


# Hauptspiel-Funktion
def game(players):
    """
    Hauptspiel-Funktion: Der Spieler muss den Titel des Artikels erraten.
    """
    print("================================================")
    print("=== 🏆 Welcome to the Wiki-Title Game! 🏆 ===")
    print("================================================")
    print("\n📝 Task: Guess the title of the article!")
    print("The title is replaced by '_' in the text, you have to guess it.\n")
    print()

    for player in players:
        article = data_handling.get_pagename()
        word_lst = check_title_in_article(article)
        section_text = get_section_text(article, word_lst)

        print(f"🎮 Player {player}, read the following paragraph and try to guess the title:")
        print()
        print(section_text)

        # Benutzerantwort
        answer = input(f"\n Player {player}, What do you think is the title of the article? ")

        # Eingabe prüfen
        if check_user_answer(answer, word_lst):
            print(f"\n🎉 Correct! The title was: {article}")
            players[player] += 1
        else:
            print(f"❌ Unfortunately wrong. The correct title was: {article}")

        # Aktualisiere den Punktestand des Spielers
        print()
        print(f"🎮 Current score of {player}: {players[player]}")
        print("-------------------------------------------")
        input("\nPress enter to continue...")
        print()
        
    return players
