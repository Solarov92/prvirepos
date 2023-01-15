sekunde = 10

import random



baterija = 90

while baterija > 0:
    print("Mozes koristiti telefon ", baterija, "%")
    baterija -= random.randint(35, 66)

    for broj in range(15):
        if broj == 6:
            continue
        print(broj)


