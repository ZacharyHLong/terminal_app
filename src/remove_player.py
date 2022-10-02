import csv
import pandas as pd 
import view_roster as vr
import exceptions as ex


# A loop that allows users to remove a player from the roster and CSV file.
def remove_loop():
    cont_loop = True
    roster = pd.read_csv('src/roster.csv', index_col ='First Name')
    vr.roster_check('remove players from')
    
    while cont_loop == True: 
        remove_player_loop = input('\nDo you want to remove a player from the roster? (y/n): ')
        if remove_player_loop == 'y':
            
            user_input = ex.removal_checker('Enter the first name of the player you would like to remove?: ')
            drop_confirmation = input('Are you sure you want to remove ' + user_input + '? (y/n): ')

            if drop_confirmation == 'y':
                roster.drop(user_input, axis = 0, inplace = True)
                roster.to_csv('src/roster.csv')
                print('\nSuccessfully removed ' + user_input +'\n')
                loop_break = input('Would you like to remove another player? (y/n): ')
                if loop_break == 'n':
                    cont_loop = False
                    break

            elif drop_confirmation == 'n':
                cont_loop = False
                break

            else:
                print('\nPlease enter either y or n. ')

        elif remove_player_loop == 'n':
            cont_loop = False
            return

        else:
            print('\nPlease enter either y or n. ')

