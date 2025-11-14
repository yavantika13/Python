import math

# Read input
A, B = map(int, input().split())

division = A / B
print(f"floor {A} / {B} = {math.floor(division)}")
print(f"ceil {A} / {B} = {math.ceil(division)}")
print(f"round {A} / {B} = {round(division)}")