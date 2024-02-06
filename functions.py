import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
# Reference from https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
from termcolor import cprint 
from pyfiglet import figlet_format

def watermark() -> str:
    print('----------------------------------------------------------------')
    print('################################################################')
    print('----------------------------------------------------------------')
    cprint(figlet_format('Chabs', font = 'starwars'),'white', attrs=['bold'])
    print('----------------------------------------------------------------')
    print('################################################################')
    print('----------------------------------------------------------------')
    return