gesamtgehalt = 0
while True:
    beschaeftigungsart = input("Beschäftigungsart: ")
    arbeitsstunden = int(input("Arbeitsstunden: "))
    if beschaeftigungsart == "Kellner":
        gesamtgehalt = gesamtgehalt + arbeitsstunden * 5
        umsatz = int(input("Umsatz: "))
        gesamtgehalt = gesamtgehalt + umsatz * 0.1
    else:
        gesamtgehalt = gesamtgehalt + arbeitsstunden * 9
    weiterer_Beschaeftigter = input("Weiterer Beschäftigter? (Ja/Nein) ")
    if weiterer_Beschaeftigter == "Ja":
        continue
    else:
        break
print(f"Gesamtgehalt: {gesamtgehalt}")