Name = ("Dupont", "Jean")  # Tuple
Hobbies = ["Tennis", "Piano", "Voyages"]  # List
client = {"Nom": Name[0], "Prénom": Name[1], "Age": 25, "Email": "sonemail@gmail.com", "Hobbies": Hobbies}  # Dictionary
# print(client["Nom"], client["Prénom"])

# faire un dictionnaire de plusieurs clients
clients = [
    {"Nom": "Dupont", "Prénom": "Jean", "Age": 25, "Email": "dupontjean@gmail.com",
     "Hobbies": ["Tennis", "Piano", "Voyages"]},
    {"Nom": "Durand", "Prénom": "Marie", "Age": 30, "Email": "durandmarie@gmail.com",
     "Hobbies": ["Cuisine", "Voyages", "Lecture"]}]
