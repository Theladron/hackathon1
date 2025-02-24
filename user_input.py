
def get_number_of_players():
    while True:
        try:
            player_number = int(input("How much players want ot play ? "))
        except ValueError:
            print("Error. Enter a number between 1-5.")
        else:
            if 0 < player_number <= 5:
                break
            else:
                print("Error. Enter a number between 1-5.")
    return player_number


def get_estimate():
    while True:
        try:
            estimate = int(input("How many words does the article contain? "))
        except ValueError:
            print("Error. Please enter a whole, positive number.")
        else:
            if estimate < 0:
                print("Error. Please enter a whole, positive number")
            else:
                break


def get_player_name(player):
    
    # wird aufgerufen mit: for player in range(player_number): user_input.get_player_name(player)
    return input(f"Enter your name, Player{player + 1}: ")


if __name__ == "__main__":
    get_players_information()