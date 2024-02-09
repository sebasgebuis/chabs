import sys, os
import functions as f

def search_price():
    os.system('cls')
    f.watermark()
    print('[0]: Return to menu \n[1]: $ \n[2]: $$-$$$ \n[3]: $$$$')
    choice = ''
    while not choice:
        choice = input()