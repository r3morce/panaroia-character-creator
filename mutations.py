import random

list = {}
list['a'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']
list['b'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']
list['c'] = ['Materieesser', 'Blob', 'Gummiknochen', 'Keine']

def get_mutation():
    random_list = random.choice(['a', 'b', 'c'])
    random_mutation = random.choice(list[random_list])
    return random_mutation + ' (' + random_list + ')'
