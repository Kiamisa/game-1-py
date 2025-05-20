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
    while chances > 0:
        print(" ".join(discovered_letter))
        print(f"\n Remaining chances: {chances}")
        print("Wrong letters: ", " ".join(wrong_letter))
        tries = input("\nType a letter: ").lower()

        if tries in word:
            i = 0
            for letter in word:
                if tries == letter:
                    discovered_letter[i] = letter
                i += 1
        else:
            chances -= 1
            wrong_letter.append(tries)
        if "_" not in discovered_letter:
            print(f"\n You win!! The word is {word}")
            break
if __name__ == "__main__":
    game()
