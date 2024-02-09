import sys, os

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
# Reference from https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
from termcolor import cprint 
from pyfiglet import figlet_format

def wait_key() -> str:
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getwch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def watermark() -> str:
    print('----------------------------------------------------------------')
    print('################################################################')
    print('----------------------------------------------------------------')
    cprint(figlet_format('Chabs', font = 'starwars'),'white', attrs=['bold'])
    print('----------------------------------------------------------------')
    print('################################################################')
    print('----------------------------------------------------------------')
    return

def reset() -> None:
    os.system('cls')
    watermark()
    return

def print_result(data) -> None:
    reset()
    print(f'{"Name":30} | {"Rating":6} | {"Price":8} | {"Reviews":7} | Address')
    for index, row in data.iterrows():
        print(f'{row["name"]:30} | {row["rating"]:6} | {row["priceLevel"]:8} | {row["numberOfReviews"]:7} | {row["address"].split(",")[0]}')
        
    print('\n[0]: Return to menu')
    choice = ''
    while not choice:
        choice = wait_key()
    return
