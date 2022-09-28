import csv
import csv_operations as co



# def loop_content():
#     first_name = input("What is the player's first name?: ")
#     last_name = input("What is the player's last name?: ")
#     jersey_number = input("What is the player's jersey number?: ")
#     phone_number = input("What is the player's phone number?: ")
#     temp_player = [first_name, last_name, jersey_number, phone_number]
#     content.append(temp_player)

def add_loop():
    content = []
    cont_loop = True
    while cont_loop == True:
        user_input = input('Would you like to add a player to the roster? (y/n): ')
        if user_input == 'y':
            first_name = input("What is the player's first name?: ")
            last_name = input("What is the player's last name?: ")
            jersey_number = input("What is the player's jersey number?: ")
            phone_number = input("What is the player's phone number?: ")
            content = [first_name, last_name, jersey_number, phone_number]
            content.append(temp_player)
        elif user_input == 'n':
            cont_loop = False
            break
        else:
            print('Please enter either y or n. ')


           
            
def add_player():
    user_input = input('Would you like to add a new player to the roster? (y/n): ')
    cont_loop = True
    while cont_loop == True:    
        if user_input == 'y':
            first_name = input("What is the player's first name?: ")
            last_name = input("What is the player's last name?: ")
            jersey_number = input("What is the player's jersey number?: ")
            phone_number = input("What is the player's phone number?: ")
            content = [first_name, last_name, jersey_number, phone_number]
            with open('roster.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(content)
            user_input = input('Would you like to add another player? (y/n): ')
        elif user_input == 'n':
            cont_loop = False
            break
        else:
            print('Please enter either y or n. ')

        





        # while co.csv_filled('roster.csv') == False:
        #     header = ['first_name', 'last_name', 'jersey_number', 'phone_number']
        #     content = []
        #     co.csv_create('roster.csv', header, content)

        # else:
            
        #     writer.writerow(content)
        #     return