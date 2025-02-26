
#   & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/PhilW/PycharmProjects/Hackathon/game2.py
import data_handling
import user_input


def word_count(data):
    word_list = data.split()                           # word_count soll num_words an main zurückgeben und main() soll num_words aufnehmen können
    num_words = len(word_list)
    return num_words


def play_game(players): 
    data, sitename = data_handling.get_complete_page()          # Daten abrufen
    num_words = word_count(data)  
    guess_dict = {}

    print("================================================")
    print("=== 🏆 Welcome to the Article Length Game! 🏆 ===")
    print("================================================")
    print(f"\n📝 Task: Guess the lenght of an Wikipedia article:")
    print()
    
    for player in players:                                            # die main() soll word_count() aufrufen und die variable Data übergeben                                       
        print(f"🎮 {player}, Guess the lenght of the Wikipedia article: {sitename}")
        user_guess = user_input.get_estimate()
        guess_dict[player] = abs(num_words - user_guess)
    sort_dict = dict(sorted(guess_dict.items(), key=lambda x: x[1])) 
    print()
    print()
    print("🌟 Players' distance to the actual length of the article:")
    for player in sort_dict:
        print(f"{player}: {sort_dict[player]}", end="   ")    
    for player in sort_dict:
        print()
        print(f"🏆 {player} has won the game! 🏆")
        players[player] += 1
        break
    print()
    print(f"The actual length of the Wikipedia article '{sitename}' was: {num_words} words.")
    print()
    print(f"🎮 Current score of {player}: {players[player]}")
    print("-------------------------------------------")
    input("\nPress enter to continue...")
    print()
    return players

