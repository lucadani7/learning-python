# Scrieti o functie care sa calculeze suma tuturor numerelor dintr-un tuplu dat.
# tuple_example = (8, 2, 3, 0, 7)
# result = 20

def suma_numere(tuplu):
    result = 0
    for elem in tuplu:
        result += elem
    return result


tuple_example = (8, 2, 3, 0, 7)
print(suma_numere(tuple_example))
