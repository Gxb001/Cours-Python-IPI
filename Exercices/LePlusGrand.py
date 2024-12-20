import random


def guess_random_nb():
    lvl_choice = int(input("Choisissez un niveau de difficulté (1, 2 ou 3): "))
    max_guess_possible = 0
    if lvl_choice == 1:
        max_guess_possible = 10
    elif lvl_choice == 2:
        max_guess_possible = 100
    else:
        max_guess_possible = 1000
    nb = random.randint(0, max_guess_possible)
    print(f"Devinez le nombre entre 0 et {max_guess_possible}")
    while True:
        guess = int(input("Entrez un nombre: "))
        if guess < nb:
            print("Trop petit")
        elif guess > nb:
            print("Trop grand")
        else:
            print("Bravo ! Vous avez trouvé le nombre.")
            break


guess_random_nb()
