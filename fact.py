# n=5
# fact = 1
# for i in range(1, n+1):
#     fact*=i
# print("factorial:",fact)  


# counts vowels and consonants
text ="in this code we will count vowels and consonents "  
vowels="aeiouAEIOU"
v_count = 0
c_count = 0
for ch in text:
    if ch.isalpha()  :
     if ch in vowels:
      v_count+=1
    else:
     c_count+=1
     print("vowels:",v_count,"consonents:",c_count)