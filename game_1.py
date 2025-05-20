import random
from os import name,system

def clear_all():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_all()

def game():

    clear_all()
    print("Bem vindo ao jogo da Forca\n")
    print("Adivinhe a palavra abaixo:\n")

    words = ['carro', 'casa', 'helicoptero', 'soldado', 'peste', 'arroba', 'python', 'java', 'windows']

    word = random.choice(words)

    discovered_letter = ['_' for letter in word]

    chances = 6

    wrong_letter = []
