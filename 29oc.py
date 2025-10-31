# n=10
# a=1
# b=5
# for i in  range(1):
#   c=a+b
#   print (a,b,c)
#   c=b
#   b=a


# def fibonacci(num):
#     return num if num<=1 else fibonacci(num-1)+ fibonacci(num-2)
# n=10
# print("fibonacci sequence")
# for num in range(n):
#     print(fibonacci(num))


# Simple Python program to find sum of series
# with cubes of first n natural numbers
# Returns the sum of series 
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i + i+i      
    return sum
n = 5
print(sumOfSeries(n))

 