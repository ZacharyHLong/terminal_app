import pandas as pd

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
            raise NumError('Only numerical characters are allowed. ')
        elif len_count == val1:
            return variable
        elif len_count == val2:
            return variable
        else:
            raise LenError(f'Integer entered must be either {val1} or {val2} digits. ')


def get_a_number(message, val1, val2):
    variable = None
    valid_input = False
    while not valid_input:
        try:
            variable = len_num_check(message, val1, val2)
            # num_char_check(variable)
        except NumError as num_err:
            print(num_err)
        except LenError as len_err:
            print(len_err)
        except ValueError:
            print('Please enter an integer. ')
        else:
            valid_input = True
            return variable



def alpha_char_check(message):
    variable = str(input(message))
    if not variable.isalpha():
        raise AlphaError('Only alphabetical characters are allowed. ')
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
            print('Please enter a name! (Alphabetical characters only). ')
        else:
            valid_input = True
            return variable



def removal_checker(message):
    roster = pd.read_csv('roster.csv', index_col = 'First Name')
    valid_input = False
    while not valid_input:
        try:
            user_input = get_a_name(message)
            print(roster)
            if user_input not in roster.values:
                raise KeyError('That player is not on the roster. Please enter a name from above. ')
            else:
                raise KeyError()
        except KeyError as err:
            KeyError(err)
        else:
            valid_input = True
            return user_input
        finally:
            print('finally')



def menu_selector():
    pass
#make sure loops dont go infintie (y or n) - keyerror

