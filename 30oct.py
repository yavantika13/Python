def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)
n=5
print("\nPrinting numbers from 1 to",n)
print_1_to_n(n)

def print_1_to_n(n):
    if n==0:
        return
    print(n)
    print_1_to_n(n-1)
n=5
print("\nPrinting numbers from 1 to",n)
print_1_to_n(n)