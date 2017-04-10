import random

list = ['Service', 'Militaer', 'Innere Sicherheit', 'Forschung und Entwicklung']
spion = 'Spion'
list.append(spion)


def get_service_group():
    result = random.choice(list)
    if result == spion:
        list.remove(spion)
        spy_group = random.choice(list)
        list.remove(spy_group)
        result = 'Spion fuer ' + spy_group + ' in ' + str(random.choice(list))

    return result
