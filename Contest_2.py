# a, b, k =map(int, input().split())
# if a ==  k and b == k:
#     print("Both")
# elif a %  k == 0:
#     print("Memo")  
# elif b %  k == 0:
#     print("Momo")
# else:
#     print("No One")        

a, b, k =map(int, input().split())
a_div = (a % k == 0)
b_div = (b % k == 0)

if a_div and b_div:
        print("Both")
elif a_div:
        print("Memo")
elif b_div:
      print ("Momo")
else:
       print("No One")