print("Bitte geben Sie zwei zahlen an die miteinander Multipliziert werden sollen.")
try:
    num1 = int(input("1. Zahl: "))
    num2 = int(input("2. Zahl: "))
    print(f"Das Produkt von {num1} und {num2} ist {num1 * num2}")
except: print("Das ist keine Zahl!")