#!/usr/bin/python

import os
import sys
import string
import random

import player
import names

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# chosen name
if len(sys.argv)>1:
    chosen_name = sys.argv[1]
else:
    chosen_name = random.choice(names.list)

# block
if len(sys.argv)>2:
    block = sys.argv[2]
else:
    block = random.choice(string.letters).upper()
    block += random.choice(string.letters).upper()
    block += random.choice(string.letters).upper()



# troubleshooter
troubleshooter = player.Troubleshooter(chosen_name, block)

# finish
print 'Paranoia Character Creator'
print ''
troubleshooter.print_sheet()
