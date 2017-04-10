#!/usr/bin/python
import os
import csv
import string
import random
from tabulate import tabulate

character = []
names = []
mutations = []
service_groups = []
secret_organizations = []

# read files
with open('names.csv', 'rb') as csvfile:
    names_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in names_csv:
        names.append(''.join(row))

with open('mutations.csv', 'rb') as csvfile:
    mutations_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in mutations_csv:
        mutations.append(''.join(row))

with open('secret_organizations.csv', 'rb') as csvfile:
    secret_organizations_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in secret_organizations_csv:
        secret_organizations.append(''.join(row))

with open('service_groups.csv', 'rb') as csvfile:
    service_groups_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in service_groups_csv:
        service_groups.append(''.join(row))

# header
print 'Paranoia Character Creator'
print ''



# chosen name
# individual_name = raw_input('Name: ')
individual_name = random.choice(names)

# clearance
clearance = "R"

# block
block = random.choice(string.letters)
block + random.choice(string.letters)
block + random.choice(string.letters)

# while True:
#     block = raw_input('Wohnblock: ')
#     if len(block) == 3:
#       break
#     else:
#       print '\tBitte nur 3 Zeichen.'


# clone
clone_nr = "1"

# name
name = individual_name + '-' + clearance +  '-' + block +  '-' + clone_nr
character.append(['Name', name])

# service
print service_groups
service_group = random.choice(service_groups)
character.append(['Servicegruppe:', service_group])

# secret organization
secret_organization = random.choice(secret_organizations)
character.append(['Geheimorganisation:', secret_organization])

# mutation
mutation = random.choice(mutations)
character.append(['Mutantenkraft:', mutation])

# finish
os.system('clear')
print tabulate(character)
