import csv 
import csv_operations


# first time initialisation
if csv_operations.csv_filled('nameteam.csv') == False:
    print('Welcome to the Team Manager Assistant, before you get underway, there are several questions you must answer.')
    manager_name = input('What is your first name? ')
    team_name = input('What is the name of your team? ')


    with open('nameteam.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'team'])
        writer.writerow([manager_name, team_name])

# welcome message
with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'Welcome {row[0]}, manager of {row[1]}')
        break

#menu
print ('1) View Roster ')
print ('2) Add Player ')
print ('3) Remove Player ')
print ('4) Teamsheet Payment ')
print ('5) Quit ')
print(' ')


menu_input = input('What would you like to do? ')
