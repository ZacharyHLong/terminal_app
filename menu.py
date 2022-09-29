import csv
import csv_operations as co
import view_roster as vr
import add_player as ap
import remove_player as rp


def return_to_menu():
    user_input = input('Would you like to return to the menu? (y/n): ')
    if user_input == 'n': 
        print('Thanks for using the Team Manager Assistant')
        quit()
    elif user_input == 'y':
        return
    else:
        print('Please enter either y or n. ')

def menu():
    print ('1) View Roster ')
    print ('2) Add Player ')
    print ('3) Remove Player ')
    print ('4) Quit ')
    print(' ')


def menu_loop():
    display_menu = True
    while display_menu == True:
        menu()
        menu_input = input('What would you like to do? ')
        if menu_input == '1':
            print('View Roster')
            vr.roster_check('view')
            return_to_menu()

        elif menu_input == '2':
            print('Add Player')
            ap.add_player()
            return_to_menu()

        elif menu_input == '3':
            rp.remove_loop()
            return_to_menu()

        elif menu_input == '4':
            print('Thanks for using the Team Manager Assistant')
            quit()
            
        else:
            print('Please enter a valid menu number. ')
            

