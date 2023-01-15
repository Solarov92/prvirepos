
pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in["marko", "milos", "marija", "ana", "sofija"]:
    print("Ime", ime)

print("Prva sledeca linija...")

for broj in [1, 2, 3, 4, 5,]:
    print("Ovo je broj:", broj)

    
    for broj in range(5, 10, 2):
        print(broj)
    for broj in range(100, 0, -7):
        print("Prikaz", broj)



    pozicija_automobila = 0
    pozicija_cilja = 10

    for kretanja in range(5):
        pozicija_automobila += 2
        print(pozicija_automobila == pozicija_cilja)

    start_date = 2010
    end_date = 2015
    print("*******Alowed years*********")
    for godine in range(2010, 2016):
        print(godine)

    print("1\t2\t3")
    print("***********************")

    for brojac in range(1, 51):

        print(brojac * 1, end="\t")
        print(brojac * 2, end="\t")
        print(brojac * 3)


    for x in range(5):
        for y in range(3):
            print("Ovo je X:", x, "Ovo je Y:", y)

    for x in range(6):
        for y in range(6):
            if x == y:
                print("*", end= " ")
            else:
                print("#", end= " ")
        print()

        for x in range(10):
            for y in range(10):
                if x == 0 or x == 9 or y == 0 or y == 9:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()
                


    

    
            







        
        