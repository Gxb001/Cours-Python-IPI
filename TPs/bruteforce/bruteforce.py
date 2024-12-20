import random
import string
import time

from tqdm import tqdm


def generetage_password(size):
    password = ''
    for i in range(size):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


def bruteforce_password(password, size, complexity=string.ascii_letters + string.digits + string.punctuation):
    nb_tries = 0
    tried_passwords = set()
    total_possible = calculate_possible_passwords(size, complexity)
    progress_bar = tqdm(total=total_possible, desc="Bruteforce Progress")
    temp_a = time.time()
    while True:
        brute = ''.join(random.choice(complexity) for _ in range(size))
        if brute in tried_passwords:
            continue
        elif brute == password:
            return brute, nb_tries, complexity, round(time.time() - temp_a)
        else:
            tried_passwords.add(brute)
            nb_tries += 1
            progress_bar.update(1)


def calculate_possible_passwords(size, complexity):
    return len(complexity) ** size


mdp_guess = generetage_password(4)
# print(f"Password: {mdp_guess}")
res = bruteforce_password(mdp_guess, 4)
print(f"Password: '{res[0]}', en {res[1]} essais, en {res[3]} secondes, avec comme complexité: {res[2]}")
