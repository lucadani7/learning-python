def impartire_numere(a, b, c):
    if b == 0 or c == 0:
        return 0
    return 3 * a / b / c if (a == b == c) else a / b / c


print(impartire_numere(28, 4, 7))
print(impartire_numere(28, 0, 4))
print(impartire_numere(2, 2, 2))
