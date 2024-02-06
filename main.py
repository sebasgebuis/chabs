import pandas as pd 
import sys
from functions import watermark

data = pd.read_csv('melbourne_ta_reviews.csv', sep = ',')

if __name__ == '__main__':
    watermark()
    while True:
        print('[0]: Quit \n[1]: Search by genre \n[2]: Search by price \n[3]: Search by name')
        key = input()
        if key == '0':
            # Exit button
            sys.exit()
        elif key == '1':
            # roep functie aan
            print('hoi')
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