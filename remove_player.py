import csv
import pandas as pd 
import view_roster as vr
import exceptions as ex


def remove_loop():
    cont_loop = True
    roster = pd.read_csv('roster.csv', index_col ='First Name')
    vr.roster_check('remove players from')
    remove_player_loop = input('Do you want to remove a player from the roster? (y/n): ')

    if remove_player_loop == 'n':
        cont_loop = False
        return

    elif remove_player_loop == 'y':
        while cont_loop == True:     
            user_input = ex.removal_checker('Enter the first name of the player you would like to remove?: ')
            # needs name checker here!!!
            drop_confirmation = input('Are you sure you want to remove ' + user_input + '? (y/n): ')

            if drop_confirmation == 'y':
                roster.drop(user_input, axis = 0, inplace = True)
                roster.to_csv('roster.csv')
                print('Successfully removed ' + user_input)
                cont_loop = False

            elif drop_confirmation == 'n':
                cont_loop = False
                break

            else:
                print('Please enter either y or n. ')
    else:
        print('Please enter either y or n. ')

