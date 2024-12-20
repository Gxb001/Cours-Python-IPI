import random


def shifumi(nb_win_rounds):
    win_rounds_user = 0  # user win points
    win_rounds_computer = 0  # computer win points
    while win_rounds_user != nb_win_rounds or win_rounds_computer != nb_win_rounds:
        user_choice = input("Choisissez entre pierre, feuille ou ciseaux: ")
        computer_choice = random.choice(["pierre", "feuille", "ciseaux"])
        print(f"L'ordinateur a choisi: {computer_choice}")
        if user_choice == computer_choice:
            print("Egalité")
        elif user_choice == "pierre" and computer_choice == "ciseaux" or user_choice == "feuille" and computer_choice == "pierre" or user_choice == "ciseaux" and computer_choice == "feuille":
            print("Vous avez gagné cette manche")
            win_rounds_user += 1
        else:
            # elif (user_choice == "pierre" and computer_choice == "feuille") or (user_choice == "feuille" and computer_choice == "ciseaux") or (user_choice == "ciseaux" and computer_choice == "pierre"):
            print("L'ordinateur a gagné cette manche")
            win_rounds_computer += 1
        if win_rounds_user == nb_win_rounds:
            print("Vous avez gagné la partie")
            break
        elif win_rounds_computer == nb_win_rounds:
            print("L'ordinateur a gagné la partie")
            break
        print("Score actuel: " + f"Vous: {win_rounds_user} - Ordinateur: {win_rounds_computer}")
    print("Score finale : " + f"Vous: {win_rounds_user} - Ordinateur: {win_rounds_computer}")


shifumi(2)
