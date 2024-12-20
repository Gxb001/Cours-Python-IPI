import random
def guess_random_nb():
    lvl_choice = int(input("Choisissez un niveau de difficulté (1, 2 ou 3): "))
    if lvl_choice == 1:
        nb = random.randint(0, 10)
    elif lvl_choice == 2:
        nb = random.randint(0, 100)
    else:
        nb = random.randint(0, 1000)
    print(f"Devinez le nombre entre 0 et {nb}")
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