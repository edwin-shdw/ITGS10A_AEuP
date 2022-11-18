import random

zahl = random.randrange(1, 200)
versuche = 1
eingabeZahl = int(input("Ihre Zahl: "))
while zahl != eingabeZahl:
    versuche = versuche + 1
    if eingabeZahl > zahl:
        print("Ihre Zahl ist größer als die gesuchte Zahl")
    else:
        print("Ihre Zahl ist kleiner als die gesuchte Zahl")
    eingabeZahl = int(input("Ihre Zahl: "))
print("Sie haben die Zahl erraten!")
print("Sie haben " + str(versuche) + " Versuche gebraucht!")