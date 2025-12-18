A, B, C, D = map(int, input().split())
Mul = A*B*C*D
last_two = Mul%100
formatted = f"{last_two:02d}"
print(formatted)