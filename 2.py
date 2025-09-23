# rows = 5
# for i in range(1, rows+1):
#     for j in range(1,i+1):
#         print(j, end= " ")
#     print()    

num = 145
total = 0
for d in str(num):
    digit = int(d)
    fact=1
    for i in range (1,digit+1):
     fact*=1
     total += fact
if total == num:
   print(f"{num} is a strong number")  
else:
       print(f"{num} is not a strong number")  


#check wheater a num divisible by its 
# check if the square of a num and by the itself
# chech weater in a number if the sum of the digits powered with their positions to that number
#        