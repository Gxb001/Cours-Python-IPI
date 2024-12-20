import random
def guess_random_nb(lvl):
    if lvl == 1:
        nb = random.randint(0, 10)
    elif lvl == 2:
        nb = random.randint(0, 100)
    else:
        nb = random.randint(0, 1000)
    print("Je pense à un nombre entre 0 et 100. Devinez-le !")
    while True:
        guess = int(input("Entrez un nombre: "))
        if guess < nb:
            print("Trop petit")
        elif guess > nb:
            print("Trop grand")
        else:
            print("Bravo ! Vous avez trouvé le nombre.")
            break
guess_random_nb(1)