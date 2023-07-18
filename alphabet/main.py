def numar_vocale():
    nr_voc = 0
    lista_vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while True:
        cuvant = input("Introdu un cuvant: ")
        if len(cuvant) < 11:
            break
        print("Lungimea cuvantului tau este " + str(len(cuvant)) + ", dar trebuie maxim 10.")
    for caracter in cuvant:
        if caracter in lista_vocale:
            nr_voc += 1
    return nr_voc


print(numar_vocale())
