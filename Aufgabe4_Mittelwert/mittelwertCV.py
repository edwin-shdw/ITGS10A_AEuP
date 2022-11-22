summe = 0
anzahl = 0
# There is no do while in py
# so this is an emulation
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