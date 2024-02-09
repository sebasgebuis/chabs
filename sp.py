import sys, os
import functions as f
import df as data

def search_price():
    f.reset()
    print('Search by price: \n[1]: $ \n[2]: $$-$$$ \n[3]: $$$$ \n[0]: Return to menu')
    choice = ''

    while not choice:
        choice = f.wait_key()

    f.reset()
    print('Order by: \n[1]: Ranking \n[2]: Rating \n[3]: Amount of reviews \n[0]: Return to menu')
    choice1 = ''
    while not choice1:
        choice1 = f.wait_key()
        if choice == '1' and choice1 == '1':
            f.print_result(data.sp_cat1_rp)
        elif choice == '1' and choice1 == '2':
            f.print_result(data.sp_cat1_rt)
        elif choice == '1' and choice1 == '3':
            f.print_result(data.sp_cat1_rv)

        elif choice == '2' and choice1 == '1':
            f.print_result(data.sp_cat2_rp)
        elif choice == '2' and choice1 == '2':
            f.print_result(data.sp_cat2_rt)
        elif choice == '2' and choice1 == '3':
            f.print_result(data.sp_cat2_rv)

        elif choice == '3' and choice1 == '1':
            f.print_result(data.sp_cat3_rp)
        elif choice == '3' and choice1 == '2':
            f.print_result(data.sp_cat3_rt)
        elif choice == '3' and choice1 == '3':
            f.print_result(data.sp_cat3_rv)