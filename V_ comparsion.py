# v_comprsion

input_line = input()


A_str, S, B_str = input_line.split()
A = int(A_str)
B = int(B_str)


if S == '<':
    result = A < B
elif S == '>':
    result = A > B
elif S == '=':
    result = A == B
else:
    result = False  

print("Right" if result else "Wrong")