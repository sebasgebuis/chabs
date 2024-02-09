import sys, os
import functions as f
import sp

if __name__ == '__main__':
    os.system('cls')
    while True:
        f.watermark()
        print('[0]: Quit \n[1]: Search by price \n[2]: Search by name \n[3]: Search by zip code')
        key = f.wait_key()
        if key == '0':
            # Exit button
            os.system('cls')
            sys.exit()
        elif key == '1':
            # roep functie aan
            sp.search_price()
        elif key == '2':
            # roep andere functie aan
            print('hoi')
        elif key == '3':
            # roep andere functie aan
            print('hoi')
        elif key == '4':
            # roep laatste functie aan
            print('hoi')
        else:
            print('Please provide a proper input')
        os.system('cls')