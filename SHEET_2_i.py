N = input()
rev = N[::-1].lstrip('0')
if rev == "":
    rev = "0"
print(rev)
if N == rev:
    print("YES")
else:
    print("NO")    
