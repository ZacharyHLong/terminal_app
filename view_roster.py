import csv
import csv_operations as co
from prettytable import from_csv

def display_roster():
    with open('roster.csv', 'r') as f:
        mytable = from_csv(f)
        print(mytable)


def roster_check():
    if co.csv_filled('roster.csv') == False:
        print('You need to add players before you can view the roster! ')
    else:
        display_roster()