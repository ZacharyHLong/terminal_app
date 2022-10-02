import csv
import csv_operations as co
from prettytable import from_csv
import pandas as pd

# Displays the user's roster information in a table
def display_roster():
    with open('nameteam.csv') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            team = f'  {row[1]}  '
            x = team.center(57, ':')
            print(x)
    
    with open('roster.csv', 'r') as f:
        mytable = from_csv(f)
        print(mytable)

# Check's to see if the user has added any players to the roster.
def roster_check(filler):
    rowcount = 0

    for row in open('roster.csv'):
        rowcount += 1
    
    if rowcount <= 1:
        print('You need to add players before you can ' + filler + ' the roster! ')
        return
    else:
        display_roster()