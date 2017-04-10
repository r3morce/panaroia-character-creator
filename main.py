#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os
import string
import random
from tabulate import tabulate

import names
import osa
import mutations
import secret_organizations
import service_groups
import items

character = []

# header
print 'Paranoia Character Creator'
print ''

# chosen name
individual_name = random.choice(names.list)

# block
block = random.choice(string.letters).upper()
block += random.choice(string.letters).upper()
block += random.choice(string.letters).upper()

# name
name = individual_name + '-' + "R" +  '-' + block +  '-' + "1"
character.append(['Name', name])

# osa
task = random.choice(osa.list)
character.append(['Obligatorische Sonderaufgabe', task])

# service group
sg_list = service_groups.list
service_group = random.choice(sg_list)

# service group spion
if service_group == sg_list[-1]:
    sg_list.remove(sg_list[-1])
    if service_group in sg_list:
        sg_list.remove(service_group)
    service_group = 'Spion fuer ' + service_group + ' in ' + ''.join(random.choice(sg_list))

character.append(['Servicegruppe', service_group])

# secret organization
so_list = secret_organizations.list
secret_organization = random.choice(so_list)

# secret organization spion
if secret_organization == so_list[-1]:
    so_list.remove(so_list[-1])
    if secret_organization in so_list:
        so_list.remove(secret_organization)
    secret_organization = 'Spion fuer ' + secret_organization + ' in ' + ''.join(random.choice(so_list))

character.append(['Geheimorganisation', secret_organization])

# mutation
mutation = random.choice(mutations.list)
character.append(['Mutantenkraft', mutation])

# finish
os.system('clear')
print tabulate(character)
print 'Ausruestung'
for item in items.basic:
    print '\t', item
