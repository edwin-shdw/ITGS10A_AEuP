summe = 0
anzahl = 0
while True:
    zahl = int(input("Zahl: "))
    summe = summe + zahl
    anzahl = anzahl + 1
    weitere_Zahl = input("Weitere Zahl? (Ja/Nein) ")
    if weitere_Zahl == "Ja":
        continue
    else:
        break
print(f"Durchschnitt: {summe/anzahl}")