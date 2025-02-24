# & C:/Users/PhilW/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/PhilW/PycharmProjects/Hackathon/denny.py
import data_handling


def remove_symbols():
    pass

def create_wordlist():
    pass

def word_count():
    pass

# word_sort():

def main():
    data = data_handling.get_complete_page()
    data = data.replace(".", "")
    data = data.replace(",", "")
    data = data.replace("!", "")
    data = data.replace("?", "")
    data = data.replace("#", "")
    data = data.replace(":", "")
    print (data)
 



if __name__ == "__main__":
    main()
