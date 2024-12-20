
#Écrire un programme qui convertit en m/h une vitesse donnée en km/h.
#Rappel : 1 mile = 1,609 k
def convertisseur(vitesse):
    vitesse = float(vitesse)
    return round(vitesse/1.609,2)

vitesse = input("Entrez une vitesse en km/h : ")
print(convertisseur(vitesse))