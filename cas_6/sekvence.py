osoba = ["sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print("godine", osoba[1])

kurs = "python"

automobili = ["Opel", "Citroen", "Mercedes"]
print(automobili[2])

duzina = len(kurs)


for x in range(len(kurs)):
    print("Na poziciji:", kurs[x])

ustanova = "IT Academy"

for x in range (len(ustanova)):
    print(ustanova[x])


primer = "zadatak1"
for indeks in range (len(primer)):
    print(primer[indeks])



broj_karaktera = len(primer)
indeks = 0

while indeks < broj_karaktera:
    print(primer[indeks])
    indeks += 1


korisnicko_ime = "admin"
uneto_kor_ime = input("Unesi korisnicko ime:")

if korisnicko_ime == uneto_kor_ime.upper():
    print("Dobrodosli")
else:
    print("Pogresni podaci")


racunar = "laptop"
model = 'MACBOOK'
racunar[1] = "C"
racunar + model 




