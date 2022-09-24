import csv
import csv_operations

def display_roster():
    with open('roster.csv', 'r') as f:
        f.seek(0)
        reader = csv.DictReader(f)
        # reader.__next__()
        for row in reader:
            print(row)


def roster_check():
    if csv_operations.csv_filled('roster.csv') == False:
        print('You need to add players before you can view the roster! ')
    else:
        display_roster()