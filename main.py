import csv 

with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'Welcome back {row[0]}')