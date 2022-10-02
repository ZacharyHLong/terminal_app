import csv
import csv_operations as co
import view_roster as vr
import add_player as ap
import remove_player as rp


# Function to format headers for each feature of the project
def menu_header(text):
    menu_item = f'  {text}  '
    x = menu_item.center(57, ':')
    print(f'\n{x}\n')

# Simple loop that allows the user to return to the menu or terminate the program
def return_to_menu():
    cont_loop = True
    while cont_loop:
        user_input = input('\nWould you like to return to the menu? (y/n): ')
        if user_input == 'n': 
            print('\nThanks for using the Team Manager Assistant!\n')
            quit()
        elif user_input == 'y':
            return
        else:
            print('\nPlease enter either y or n. ')

# The menu, with header function
def menu():
    menu_header('Menu')
    print ('   1) View Roster \n')
    print ('   2) Add Player \n')
    print ('   3) Remove Player \n')
    print ('   4) Quit \n')

# A loop made to allow users to select a menu option
def menu_loop():
    display_menu = True
    while display_menu == True:
        menu()
        menu_input = input('What would you like to do?\nType in the corresponding menu number: ')
        if menu_input == '1':
            menu_header('View Roster')
            vr.roster_check('view')
            return_to_menu()

        elif menu_input == '2':
            menu_header('Add Player')
            ap.add_player()
            return_to_menu()

        elif menu_input == '3':
            menu_header('Remove Player')
            rp.remove_loop()
            return_to_menu()

        elif menu_input == '4':
            print('\nThanks for using the Team Manager Assistant!\n')
            quit()
            
        else:
            print('\nPlease enter a valid menu number. ')
            