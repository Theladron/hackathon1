import user_input
import Wiki_title
import GuessTheWord
import Article_length
import random
import shuffle

def create_players():
    player_number = user_input.get_number_of_players()
    player_dict = {}

    # Spielerinfos sammel und Dictionary erstellen
    for player in range(player_number):
        name = user_input.get_player_name(player)
        player_dict[name] = 0
    return player_dict
    

def choose_game(player_dict, last_game): 
    games = [Article_length.play_game,GuessTheWord.play_game,Wiki_title.game,shuffle.main]

    while True:
        game_to_play = random.choice(games)
        if game_to_play != last_game:
            last_game = game_to_play
            break

    game_to_play(player_dict)
    return player_dict, last_game


def play_game():
    player_dict = create_players()
    max_score = user_input.get_max_score()
    last_game = ""
    while True:
        player_dict, last_game = choose_game(player_dict, last_game)
        # Anzeige Endergebnis
        print("Current score: ")
        for player in player_dict:
            print(f"{player} : {player_dict[player]}", end="    ")
        input("\nPress enter to continue...")
        for player in player_dict:
            if max_score <= player_dict[player]:
                sort_dict = dict(sorted(player_dict.items(), key=lambda x: x[1], reverse=True))
                winner_value = 0
                for winner in sort_dict:
                    if winner_value <= sort_dict[winner]:
                        winner_value = sort_dict.get(winner)
                        print(f"Congratulations. {player} won!")
                        input("\n\n Press enter to exit.")
                        exit()
