import sys

PERSON_COUNT = 3
persons = []
persons_sum = int()

try:
    for i in range(PERSON_COUNT):
        persons.append(int(input(f"Einsatz von Person {i+1} eingeben: ")))
        persons_sum += persons[i]
    win_val = int(input("Bitte den zu verteilenden Gewinn eingeben: "))
except: sys.exit("Das ist eine ungültige Zahl!")

for i in range(PERSON_COUNT):
    print(f"Person {i+1} erhält: {persons[i] / persons_sum * win_val}")
