from pyfiglet import Figlet
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_banner(text: str = "Password Scrambler", font: str = "slant") -> str:
    """
    Generate and return an ASCII art banner using pyfiglet in red color.
    
    Args:
        text (str): The text to display in the banner
        font (str): The font to use (default: 'slant')
        
    Returns:
        str: The red ASCII art banner
    """
    try:
        figlet = Figlet(font=font)
        ascii_art = figlet.renderText(text)
        return f"{Fore.RED}{ascii_art}{Style.RESET_ALL}"
    except Exception as e:
        # Fallback to a simple banner if pyfiglet fails
        return f"\n{'=' * 50}\n{text.center(50)}\n{'=' * 50}\n"
