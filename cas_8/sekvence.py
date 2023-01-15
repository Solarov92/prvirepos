
# brojevi = [9, 1, 3, 2, 5, 8, 7]

# brojevi.sort()
# print(brojevi)

brojevi = [9, 1, 3, 2, 5, 8, 7]
while True:
    izvrsena_zamena = False
    for i in range(1, len(brojevi)):
        if brojevi[i] < brojevi[i-1]:
            privremena = brojevi[i]
            brojevi[i] = brojevi[i-1]
            brojevi[i-1] = privremena
            izvrsena_zamena = True
    if izvrsena_zamena == False:
        break
print(brojevi)   




