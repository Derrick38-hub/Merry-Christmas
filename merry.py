print("""
    *    *
  *  🎄  *
 * Merry   *
* Christmas *
   *    *
""")


import pyfiglet
from colorama import Fore, Style

ascii_art = pyfiglet.figlet_format("Merry Christmas")

print(Fore.RED + ascii_art + Style.RESET_ALL)
