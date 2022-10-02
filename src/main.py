import csv 
import csv_operations as co
import pandas as pd
import view_roster
import menu
import exceptions as ex
import random
from prettytable import from_csv


# First time initialisation
if co.csv_filled('nameteam.csv') == False:
    print('\nWelcome to the Team Manager Assistant, before you get underway, there are several questions you must answer.')
    manager_name = ex.get_a_name('What is your first name? ')
    team_name = ex.get_a_name('What is the name of your team? ')
    content = [manager_name, team_name]
    header = ['name', 'team']

    co.csv_create('nameteam.csv', header, content)

# Welcome message
with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'\nWelcome {row[0]}, manager of {row[1]}')
        break

# Menu
menu.menu_loop()



