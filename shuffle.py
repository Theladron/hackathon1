from sys import displayhook

import data_handling
import random
import re
import colored_text
import user_input
import wikipedia


WIKI_LANGUAGE = "en"
SUMMARY_SENTENCES = 1
GREEN = '\033[92m'
BOLD = '\033[1m'
ENDC = '\033[0m'

#players = 
original_list = []
template_list = []
template = ""
original = ""
shuffled = ""
hint = ""


def find_random_title():                        # muß noch in data_handling verschoben werden
    wikipedia.set_lang(WIKI_LANGUAGE)
    title = wikipedia.random(pages = 1)
    return title


def request_apt_summary(title):
    wikipedia.set_lang(WIKI_LANGUAGE)
    try:
        summary = wikipedia.summary(title, auto_suggest = False, sentences = SUMMARY_SENTENCES)
        #summary = data_handling.get_page_summary(title, sentences = SUMMARY_SENTENCES)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        new_title = random.choice(e.options)
        #summary = data_handling.get_page_summary(new_title, sentences = SUMMARY_SENTENCES)
        summary = wikipedia.summary(title, auto_suggest = False, sentences = SUMMARY_SENTENCES)
    except HTTPTimeoutError:
        new_title = find_random_title()
        #summary = data_handling.get_page_summary(new_title, sentences = SUMMARY_SENTENCES)
        summary = wikipedia.summary(title, auto_suggest = False, sentences = SUMMARY_SENTENCES)
    except RedirectError:
        new_title = find_random_title()
        #summary = data_handling.get_page_summary(new_title, sentences = SUMMARY_SENTENCES)
        summary = wikipedia.summary(title, auto_suggest = False, sentences = SUMMARY_SENTENCES)
    return summary


def create_hint_for_title(title, summary):
    #colored_text.print_dark_grey(title)
    #colored_text.print_dark_grey(summary)
    buzzlist = [" is ", " was "]
    for word in summary.split():
        if word[-2:] == 'ed' and word[0] == word[0].lower():  # vermute einfach mal hier das verb!
            buzzlist.append(word)
            #print(buzzlist)
    for buzzword in buzzlist:
        try:
            buzz_start = summary.find(buzzword)
        except UnboundLocalError:
            return "No hint available"
    hint = "..." + summary[buzz_start:]
    if len(hint) < 5:
        return "No hint available"
    return hint


def insert_character_into_template(original_list, template_list, char):
    #print(f"from insert: {original_list, template_list, char}")
    for element in range(len(template_list)):
        #print(f"criteria: {original_list[element].lower(), char.lower()}") #debug
        if original_list[element].lower() == char.lower():
            template_list[element] = original_list[element]
        else:
            continue
    template = "".join(template_list)
    return template


def praise_winner(player):
     wintext = "and the winner is"
     praise = "Praise him and his heirs of the next 5 generations!"
     colored_text.print_yellow(f"{' ' * int((60-len(wintext))/2)}{wintext}{' ' * int((60-len(wintext))/2)}")
     colored_text.print_yellow(f"{'*' * 60}")
     colored_text.print_yellow_bold(f"*{' ' * int((58-len(player))/2)}{player}{' ' * int((58-len(player))/2)}*")
     colored_text.print_yellow(f"{'*' * 60}")
     colored_text.print_yellow(f"{' ' * int((60-len(praise))/2)}{praise}{' ' * int((60-len(praise))/2)}")
     return player


def create_shuffled_title(text):
    words = text.split()
    shuffled_list = []
    for word in words:
        chars = list(word)
        random.shuffle(chars)
        shuffled_word = "".join(chars)
        shuffled_list.append(shuffled_word + " ")
    return "".join(shuffled_list)


def ask_for_solution(player, original):
    solution = input(f"{player}: Enter the complete title for points, glory and celebrations! ")
    #print(f"from solution poll: {solution, original}")
    if solution.lower() == original.lower():
        return player
        
    else:
        print(f"Ooops! {player} found only the Zonk!")
    return -1

def sell_character_to_player(player, original_list, template_list):
    #print(f"from sell: {original_list, template_list}")   #debug
    while True:
        char = input(f"Which character do you want to insert? ")

        if char.lower() not in "abcdefghijklmnopqrstuvwxyz":
            print("Numbers and special characters are for free and already inserted.")
        elif char.lower in template_list:
            print("This character is already present. This round is forfeit for you!")
            return "".join(template_list)
        else:
            insert_character_into_template(original_list, template_list, char)
            #print(template)  #debug
            return template

MENU = {'solve': ask_for_solution, 'buy': sell_character_to_player}

def initiate_playground():
    page_fault = True
    while page_fault:
        title = find_random_title()
        summary = request_apt_summary(title)
        page_fault = False
        hint = create_hint_for_title(title, summary)
    original_list = list(title)
    template = re.sub('[a-zA-Z]', '_', title)  # numbers are intentionally left alone!
    template_list = list(template)
    shuffled = create_shuffled_title(title)

    #colored_text.print_red(f"\n {template}\n")
    #colored_text.print_cyan(shuffled.strip())
    #print()
    #colored_text.print_light_grey(hint)
    return original_list, template_list, hint, shuffled


def print_display(template, hint, shuffled):
    colored_text.print_red(template)
    colored_text.print_dark_grey(hint)
    colored_text.print_blue(shuffled)


def get_players_choice(player):
    while True:
        print_display(template, hint, shuffled)
        players_choice = input(f"Player {player}: Enter your choice: {GREEN}{BOLD}s{ENDC}olve or {GREEN}{BOLD}b{ENDC}uy? ")
        if players_choice.lower() in ['s', 'solve']:
            return "solve"
        elif players_choice.lower() in ['b', 'buy']:
            return "buy"




def main(players):
    #players = ['Alf', 'Berta', 'Carl']
    #original_list = []
    #template_list = []
    #template = ""
    original = ""
    #shuffled = ""
    #hint = ""
    print("================================================")
    print("======= 🏆 Welcome to the Shuffle Game! 🏆 ======")
    print("================================================")
    print(f"\n📝 Task: Solve or buy characters to geht the Word!")
    win_condition = False
    original_list, template_list, hint, shuffled = initiate_playground()
    template = "".join(template_list)
    while not win_condition:
        for player in players:
            print_display(template, hint, shuffled)
            #print(f"from main: {template_list}") #debug
            #print(f"from main: {original_list}") #debug
            #template = "".join(template_list)
            #print(template)
            choice = get_players_choice(player)
            #print(choice)
            original = "".join(original_list)
            #print(f"from main: {original}")
            if choice == 'solve':
                winner = ask_for_solution(player, original)
                praise_winner(winner)
                players[winner] += 3
                win_condition = True 
            else:
                sell_character_to_player(player, original_list, template_list)
            #print(f"dito from main: {original_list, template_list}") #debug
            template = "".join(template_list)
            #print(template)
    return players


if __name__ == "__main__":
    main()







