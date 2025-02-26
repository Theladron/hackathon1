def get_max_score():
    while True:
        try:
            max_score = int(input("Enter maximum points to win: "))
        except ValueError:
            print("Error. Enter a number between 1-1000.")
        else:
            if 0 < max_score <= 1000:
                break
            else:
                print("Error. Enter a number between 1-1000.")
    return max_score   


def get_number_of_players():
    while True:
        try:
            player_number = int(input("How many players want to play ? "))
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
    return estimate


def get_player_name(player):
    while True:
        try:
            # wird aufgerufen mit: for player in range(player_number): user_input.get_player_name(player)
            name = input(f"Enter your name, Player {player + 1}: ")
        except ValueError:
            print("Error. Please enter a valid username.")
        else:
            if name == "":
                print("Please enter an username. Cant be empty")
            else:
                break
    return name

