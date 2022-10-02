import csv
import csv_operations as co
import exceptions as ex
           
# A loop that contains several functions in order to get accurate information when adding a player, and then saves it to a CSV file            
def add_player():
    cont_loop = True
    while cont_loop == True:
        user_input = input('Would you like to add a new player to the roster? (y/n): ')    
        if user_input == 'y':

            first_name = ex.get_a_name("\nWhat is the player's first name?: ")
            last_name = ex.get_a_name("What is the player's last name?: ")
            jersey_number = ex.get_a_number("What is the player's jersey number?: ", 1, 2)
            phone_number = ex.get_a_number("What is the player's phone number?: ", 8, 10)

            content = [first_name, last_name, jersey_number, phone_number]

            with open('roster.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(content)
            user_input = input('\nWould you like to add another player? (y/n): ')

        elif user_input == 'n':
            cont_loop = False
            break

        else:
            print('\nPlease enter either y or n. \n')