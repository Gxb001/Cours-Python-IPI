def sum_list():
    notes = []
    val = 0
    while val >= 0:
        try:
            val = float(input("Entrez une note: "))
            if val >= 0:
                notes.append(val)
        except ValueError:
            print("Veuillez entrer un nombre valide")
    print(notes)
    return sum(notes) / len(notes), len(notes)


res = sum_list()
print(f"La moyenne des notes est {res[0]} pour {res[1]} notes.")
