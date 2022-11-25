import sys

TAX = 0.19    # 19%

print("Bitte geben Sie einen Rechnungsbetrag (brutto) und einen Rabattsatz an")
try:
    bill = float(input("Rechnungsbetrag: "))
    discount = int(input("Rabattsatz: ")) / 100
except:
    sys.exit("Das ist keine gültige Eingabe!")

bill = bill * (1-discount)
tax_val = bill / (100 + TAX*100) * (TAX * 100)
bill_netto = bill - tax_val

print("\nIhr Ergebnis: ")
print(f"Nettobetrag: {bill_netto:.2f}\nUmsatzsteuer: {tax_val:.2f}\nBruttobetrag: {bill:.2f}")
