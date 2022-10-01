import pandas as pd
import csv

class LenError(Exception):
   pass

class AlphaError(Exception):
    pass

class NumError(Exception):
    pass

def len_num_check(message, val1, val2):
    variable = input(str(message))
    len_count = len(variable)
    while True:
        if not variable.isnumeric():
            raise NumError('\nOnly numerical characters are allowed. \n')
        elif len_count == val1:
            return variable
        elif len_count == val2:
            return variable
        else:
            raise LenError(f'\nInteger entered must be either {val1} or {val2} digits. \n')


def get_a_number(message, val1, val2):
    variable = None
    valid_input = False
    while not valid_input:
        try:
            variable = len_num_check(message, val1, val2)
        except NumError as num_err:
            print(num_err)
        except LenError as len_err:
            print(len_err)
        except ValueError:
            print('\nPlease enter an integer. \n')
        else:
            valid_input = True
            return variable



def alpha_char_check(message):
    variable = str(input(message))
    if not variable.isalpha():
        raise AlphaError('\nOnly alphabetical characters are allowed. \n')
    else:
        return variable.title()


def get_a_name(message):
    variable = None
    valid_input = False
    while not valid_input:
        try:
            variable = alpha_char_check(message)
            if variable.isalpha():
                return variable
        except AlphaError as err:
            print(err)
        except ValueError:
            print('\nPlease enter a name! (Alphabetical characters only). \n')
        else:
            valid_input = True
            return variable



def removal_checker(message):
    roster = pd.read_csv('roster.csv')
    first_names = roster['First Name']
    valid_input = False
    while not valid_input:
        try:
            user_input = get_a_name(message)
            for i in first_names:
                if user_input == i:
                    valid_input = True
                    return user_input
            else:
                raise KeyError
               
        except KeyError as err:
            print('\nPlease enter the name of a player on the roster\n')




def menu_selector():
    pass
#make sure loops dont go infintie (y or n) - keyerror

