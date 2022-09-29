def get_a_number(message):
    pass

# include a len feature for different length numbers
# only accept integers
# menu input?

def get_a_name(message):
    variable = None
    
    try:
        variable = str(input(message))
    except ValueError:
        print('Please enter a name! (Alphabetical characters only')
    
    return variable
#capitilise name?


def removal_checker():
    pass
#make sure player is in the list of players

def menu_selector():
    pass
#make sure loops dont go infintie (y or n)

