# Read input
A, B, C = map(int, input().split())

# Store original and sorted lists
original = [A, B, C]
sorted_values = sorted(original)

# Print sorted values
for value in sorted_values:
    print(value)

# Print blank line
print()

# Print original values
for value in original:
    print(value)