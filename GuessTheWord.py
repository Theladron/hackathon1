# & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/PhilW/PycharmProjects/Hackathon/denny.py"
import data_handling


def remove_symbols(data):
    data = data.replace(".", "")
    data = data.replace(",", "")
    data = data.replace("!", "")
    data = data.replace("?", "")
    data = data.replace("#", "")
    data = data.replace(":", "")
    return data

def create_wordlist(cleaned_text): 
    cleaned_text = cleaned_text.lower()
    words = cleaned_text.split()
    return words

def word_count(word_list):
    stopwords = {"and", "or", "a", "the", "of", "in", "to","for", "on","with","at","by","an","is","it","as","that","was","are"}
    filtered_words = [word for word in word_list if word and word not in stopwords]
    word_dict = {}
    for word in filtered_words:
        word_dict[word] = word_dict.get(word, 0) +1
    sort_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    return sort_dict
    

def create_toplist(sorted_words):
    counter = 0
    toplist = []
    for word in sorted_words:
        toplist.append(word)
        counter += 1
        if counter == 5:
            break
    return toplist        
 

def play_game(player_dict):
    for player in player_dict:
        data, pagename = data_handling.get_complete_page()  # Hole den Text
        pagename = pagename.replace("_", " ")
        cleaned_text = remove_symbols(data)  # Entferne Symbole
        word_list = create_wordlist(cleaned_text)  # Erstelle eine Wortliste
        word_dict = word_count(word_list)  # Zähle die Wörter
        top_words_list = create_toplist(word_dict)
        score = 0
        attempts = 5  # Anzahl der Rateversuche
    
        print("================================================")
        print("=== 🏆 Welcome to the Guess the Word Game! 🏆 ===")
        print("================================================")
        print(f"\n📝 Task: Guess the top 5 words in the wikipedia article {pagename}.")

        for attempt in range(1, attempts + 1):
            guess = input(f"🎮 {player}, your Word: ").replace(" ","").lower()
        
            if guess in top_words_list:
                print(f"\n🎉 Correct! You beecome +1 Point",  end="    ")
                score += 1
                top_words_list.remove(guess)
            else:
                print(f"❌ Unfortunately wrong. You Word is not in the Top-5", end="    ")
            print(f"Remaining attempts:{5-attempt}")    
                
        player_dict[player] += score
        print()
        print("⏹️  Out of attempts!  ⏹️")
        print("The correct words were:\n")  
        counter = 0
        for word in word_dict:
            print(f"{word}: {word_dict[word]} times", end="    ")
            counter += 1
            if counter == 5:
                break
        print()
        print(f"🎮 Current score of {player}: {player_dict[player]}")
        print("-------------------------------------------")
        input("\nPress enter to continue...")
        print()
    return player_dict

