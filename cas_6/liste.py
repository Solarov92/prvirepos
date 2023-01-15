osoba = ["Sofija", 25, "plava", False]

for x in range (len(osoba)):
    print(osoba[x])

for osobina in osoba:
    print(osobina)


voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)
    print("Na indeksu ??? nalazi se...", stavka)


for y in range(len(voce_i_povrce)):
    print(voce_i_povrce[y])

for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)


automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel"]

for pozicija, auto in enumerate(automobili):
    if auto == "Opel":
        print(pozicija, auto)

    print("pozicija:",pozicija, "auto:", auto)

automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia"

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)

automobili.pop(0)
print(automobili)

automobili[0]
broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga opel")
        broj_opela += 1
print("Imam ", broj_opela, "na placu.")


automobili.clear()
print(automobili)


automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot","Audi"]

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])


print(automobili_akcija)

automobili_akcija = automobili[1:4:2]
print(automobili_akcija)

brojevi = [1, 2, 4, 5, 7, 9, 12, 13]
parni = []
neparni = []

for broj in brojevi:
    parni.append(broj) if broj % 2 == 0 else neparni.append(broj)
    


print(parni, neparni)




