import sys

TAX = 0.19    # 19%

print("Bitte geben Sie einen Rechnungsbetrag (brutto) und einen Rabattsatz an")
try:
    bill = float(input("Rechnungsbetrag: "))
    discount = int(input("Rabattsatz: ")) / 100
except:
    sys.exit("Das ist keine gültige Eingabe!")

bill = bill * (1-discount)
tax_val = bill * TAX
bill_netto = bill * (1-TAX)

print("\nIhr Ergebnis: ")
print(f"Nettobetrag: {bill_netto}\nUmsatzsteuer: {tax_val}\nBruttobetrag: {bill}")