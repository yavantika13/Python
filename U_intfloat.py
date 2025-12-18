# Read input
N = input()

# Convert to float
num = float(N)

# Check if it's an integer
if num.is_integer():
    print(f"int {int(num)}")
else:
    integer_part = int(num)
    decimal_part = num - integer_part
    print(f"float {integer_part} {decimal_part}")