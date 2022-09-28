import csv 
import csv_operations as co
import pandas as pd
import view_roster
import menu
from prettytable import from_csv


# first time initialisation
if co.csv_filled('nameteam.csv') == False:
    print('Welcome to the Team Manager Assistant, before you get underway, there are several questions you must answer.')
    manager_name = input('What is your first name? ')
    team_name = input('What is the name of your team? ')
    content = [manager_name, team_name]
    header = ['name', 'team']

    co.csv_create('nameteam.csv', header, content)


# welcome message
with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'Welcome {row[0]}, manager of {row[1]}')
        break

#menu
menu.menu_loop()



