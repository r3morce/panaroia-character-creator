import random

list = {}
list['Unnatuerlich'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']
list['Gefaerlich'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']
list['Wiederlich'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']

def get_mutation():
    random_list = random.choice(['Unnatuerlich', 'Gefaerlich', 'Wiederlich'])
    random_mutation = random.choice(list[random_list])
    return random_mutation + ' (' + random_list + ')'
