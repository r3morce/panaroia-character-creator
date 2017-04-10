import csv

list = []

with open('names.csv', 'rb') as csvfile:
    names_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in names_csv:
        list.append(''.join(row))
