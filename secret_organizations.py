import random

list = ['Xavier School', 'SAUBER', 'Happy', 'Molez']
spion = 'Spion'
list.append(spion)

def get_secret_organizaton():
    result = random.choice(list)
    if result == spion:
        list.remove(spion)
        spy_organization = random.choice(list)
        list.remove(spy_organization)
        result = 'Spion fuer ' + spy_organization + ' in ' + str(random.choice(list))
    return result
