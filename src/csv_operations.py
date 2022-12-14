import csv

# A function that checks if a CSV file already contains information.
def csv_filled(file):
    with open(file, 'r') as f:
        f.seek(0)
        existing_lines = csv.reader(f)
        count = 0
        for line in existing_lines:
            count += 1
            break

        if count > 0:
            return True
        else: 
            return False

# Creates a CSV file for the initialisation of the program.
def csv_create(file, header_list, content_list):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header_list)
        writer.writerow(content_list)

