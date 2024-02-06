import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def watermark() -> str:
    print('----------------------------------------------------------------')
    cprint(figlet_format('Chabs', font = 'starwars'),'white', attrs=['bold'])
    print('----------------------------------------------------------------')
    return