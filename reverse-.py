# def rev(n):
#     return int(str(n)[::-1])

# def reversed_sum(a, b):
#     rev_a = rev(a)
#     rev_b = rev(b)
#     total = rev_a + rev_b
#     return rev(total)

# # Read input
# N = int(input())
# for _ in range(N):
#     a, b = input().split()
#     print(reversed_sum(a, b))

def rev(n):
    return int(str(n)[::-1])
    # a = rev(a)
    # b = rev(b)
    # s = a + b
N = int(input())
for _ in range(N):
    a, b = input().split()
    a = rev(a)
    b = rev(b)
    s = a + b
    print(rev(s))