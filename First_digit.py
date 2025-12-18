# Read input
X = input().strip()

# Get the first digit
first_digit = int(X[0])


if first_digit % 2 == 0:
    print("EVEN")
else:
    print("ODD")