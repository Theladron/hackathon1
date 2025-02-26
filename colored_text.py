#coloring console output using ANSII-sequences thus independent from modules
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_red(text):
    print("\033[0;91m {}\033[00m".format(text))

def print_red_bold(text):
    print("\033[1;91m {}\033[00m".format(text))

def print_green(text):
    print("\033[92m {}\033[00m".format(text))

def print_yellow(text):
    print("\033[0;93m {}\033[00m".format(text))

def print_yellow_bold(text):
    print("\033[1;93m {}\033[00m".format(text))

def print_blue(text):
    print("\033[94m {}\033[00m".format(text))

def print_purple(text):
    print("\033[95m {}\033[00m" .format(text))

def print_cyan(text):
    print("\033[96m {}\033[00m".format(text))

def print_light_grey(text):
    print("\033[97m {}\033[00m".format(text))

def print_dark_grey(text):
    print("\033[90m {}\033[00m".format(text))

def main():
    print_green("Noch mehr Konsolentext")
    print_cyan("test cyan")


if __name__ == "__main__":
    main()