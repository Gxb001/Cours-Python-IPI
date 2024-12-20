import random
def guess_random_nb():
    nb = random.randint(0, 100)
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
guess_random_nb()