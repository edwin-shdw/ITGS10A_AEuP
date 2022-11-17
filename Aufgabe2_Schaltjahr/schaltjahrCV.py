jahr = int(input("Jahr: "))
if jahr >= 1582:
    if jahr%4 == 0:
        if jahr%100 == 0:
            if jahr%400 == 0:
                print("Ist ein Schaltjahr")
            else: print("Ist kein Schaltjahr")
        else:
            print("Ist ein Schaltjahr")
    else:
        print("Ist kein Schaltjahr")
else:
    print("Ist kein Schaltjahr")