import csv
import csv_operations as co
from prettytable import from_csv
import pandas as pd

def display_roster():
    with open('roster.csv', 'r') as f:
        mytable = from_csv(f)
        print(mytable)


def roster_check():
    rowcount = 0

    for row in open('roster.csv'):
        rowcount += 1
    
    if rowcount <= 1:
        print('You need to add players before you can view the roster! ')
        return
    else:
        display_roster()