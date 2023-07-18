# Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
# Sa se insereze in acest sir dupa fiecare element par, dublul acestuia (2 puncte)

def inserare_lista(my_list):
    my_final_list = []
    for elem in my_list:
        my_final_list.append(elem)
        if elem % 2 == 0:
            my_final_list.append(elem * 2)
    return my_final_list


my_list = [1, 2, 3, 4, 5, 6, 7]
print(inserare_lista(my_list))
