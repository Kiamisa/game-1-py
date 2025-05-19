import random
from os import name,system

def clear_all():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_all()