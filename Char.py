X=input()
if X.islower():
    print(chr(ord(X) - 32))  # Convert to uppercase using ASCII
else:
    print(chr(ord(X) + 32))  # Convert to lowercase using ASCII


    #print (x.upper)/print(x.lower)