import random

list = ['Teamfuehrer', 'Loyalitaetsoffizier', 'Ausruestungsbursche', 'Hyieneoffizier', 'Dokumentationsoffizier']
spion = 'Spion'
list.append(spion)

def get_osa():
    return random.choice(list)
