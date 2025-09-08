values =[0," ",None,"hi,123"]
print("AND Operators:")
for a in values:
    for  b in values:
        print(f"{a!r} and {b!r} ->{a and b!r}")
        print("\n OR Operator")
        for a in  values:
            for b in values:
                print(f"{a!r} or {b!r} ->{a or b!r}")
        print("\n NOT Operator")
        for a in  values:
             print(f"{a!r} -> {not a!r}")