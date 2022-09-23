import csv 




print('Welcome to the Team Manager Assistant, before you get underway, there are several questions you must answer.')
manager_name = input('What is your first name? ')
namelist.append(manager_name)
team_name = input('What is the name of your team? ')
namelist.append(team_name)


with open('nameteam.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([manager_name, team_name])


with open('nameteam.csv') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        print(f'Welcome back {row[0]}, manager of {row[1]}')