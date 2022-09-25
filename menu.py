import csv
import csv_operations as co
import view_roster
import add_player as ap


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
    print ('4) Teamsheet Payment ')
    print ('5) Quit ')
    print(' ')


def menu_loop():
    display_menu = True
    while display_menu == True:
        menu()
        menu_input = input('What would you like to do? ')
        if menu_input == '1':
            print('View Roster')
            view_roster.roster_check()
            return_to_menu()

        elif menu_input == '2':
            print('Add Player')
            ap.add_player()
            return_to_menu()

        elif menu_input == '3':
            print('3')
            return_to_menu()

        elif menu_input == '4':
            print('4')
            return_to_menu()

        elif menu_input == '5':
            print('Thanks for using the Team Manager Assistant')
            quit()
            
        else:
            print('Please enter a valid menu number. ')
            

