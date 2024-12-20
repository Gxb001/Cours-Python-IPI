def distinct_list(liste):
    return list(set(liste))


def distinct_list2(liste):
    distinct = []
    for i in liste:
        if i not in distinct:
            distinct.append(i)
    return distinct


def multiply_list(number):
    liste = [0 * number for i in range(10)]
    for i in range(10):
        liste[i] = (i + 1) * number
        if liste[i] % 3 == 0:
            liste[i] = f"{liste[i]}*"
    return liste


print(multiply_list(5))

print(distinct_list([1, 2, 3, 4, 5, 5, 5, 6, 7, 8]))
print(distinct_list2([1, 2, 3, 4, 5, 5, 5, 6, 7, 8]))
