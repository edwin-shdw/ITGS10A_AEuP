zahl = int(input("Zahl: "))
min = zahl
max = zahl
weitermachen = input("Weitermachen? (Ja/Nein) ")
while weitermachen == "Ja":
    zahl = int(input("Zahl: "))
    if zahl < min:
        min = zahl
    else:
        if zahl > max:
            max = zahl
    weitermachen = input("Weitermachen? (Ja/Nein) ")
print(f"Min: {min}\nMax: {max}")