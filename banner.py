from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True) # this makes sure the whole console isn't red

def print_banner():
    f = Figlet(font='slant')
    banner = f.renderText('Password Generator')
    print(Fore.GREEN + banner + Style.RESET_ALL) 