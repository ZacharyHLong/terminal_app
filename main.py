import csv 
import csv_operations



if csv_operations.csv_filled() == False:
    print('Welcome to the Team Manager Assistant, before you get underway, there are several questions you must answer.')
    manager_name = input('What is your first name? ')
    team_name = input('What is the name of your team? ')


    with open('nameteam.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'team'])
        writer.writerow([manager_name, team_name])


with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'Welcome {row[0]}, manager of {row[1]}')
        break
