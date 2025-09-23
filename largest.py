# number=[5,9,2,11,7]
# largest = number[0]
# for num in number:
#     if num > largest:
#         largest=num
# print("largest:",largest)

# prime number check

num =29
is_prime = True 
for i in range(2, num):
 if num%i ==0:
    is_prime = False
    break
print(num, "is prime?", is_prime)