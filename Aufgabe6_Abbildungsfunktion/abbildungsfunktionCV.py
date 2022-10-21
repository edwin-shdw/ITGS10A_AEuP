zahl = int(input("Zahl: "))
summe = 0
for i in range(11):
    produkt = zahl * i
    if produkt%2 == 0:
        summe = summe + produkt
print(f"Summe: {summe}")