#!/usr/bin/python

import os
import string
import random
import player
import names

# chosen name
chosen_name = random.choice(names.list)

# block
block = random.choice(string.letters).upper()
block += random.choice(string.letters).upper()
block += random.choice(string.letters).upper()

# troubleshooter
troubleshooter = player.Troubleshooter(chosen_name, block)

# finish
print 'Paranoia Character Creator'
print ''
troubleshooter.print_sheet()
