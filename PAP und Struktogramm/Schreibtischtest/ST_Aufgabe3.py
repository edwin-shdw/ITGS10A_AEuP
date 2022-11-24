a = 1
b = 0
for i in range(11):
    if i%3 == 0:
        a = a + i
    else:
        b = b + a
print(f"a: {a}\nb: {b}")