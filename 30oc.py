# n1 = 6789
# rev = 0

# while n1 > 0:
#     digit = n1 % 10
#     rev = rev * 10 + digit
#     n1 //= 10

# print(6789)
# print(rev)

# def fibonacci(num):
#  return num if num<=1 else fibonacci(num-1)+ fibonacci(num-2)
#  n=10
#  print("fibonacci sequence")
#  for num in range(n):
#    print(fibonacci(num))


# def nthEvenFibonacci(n):
#     if n == 1:
#         return 2
    
#     prev = 0  
#     curr = 2  
    
#     for i in range(2, n + 1):
        
#         next_even_fib = 4 * curr + prev
#         prev = curr
#         curr = next_even_fib
    
#     return curr

# if __name__ == "__main__":
#     n = 2 
#     result = nthEvenFibonacci(n)  
#     print(result)

def even_fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        if a > limit:
            break
        if a % 2 == 0:
            print(a)
        a, b = b, a + b


even_fibonacci(10)