dienstalter = int(input("Dienstalter: "))
alter = int(input("Alter: "))
if dienstalter >= 6:
    praemie = 80 + dienstalter * 20
    if alter > 50:
        praemie = praemie + 50
else:
    if dienstalter >= 1:
        praemie = 200
    else:
        praemie = 0
print(f"Die prämie beträgt {praemie}€")