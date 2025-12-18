N = int(input())
arr = list(map(int , input().split()))
even = 0
odd = 0
positive = 0
negative = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd +=1
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")



