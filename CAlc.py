exp=input()
# for oprends in '+-*/':
#    if oprends in exp:
#     A, B = exp.split(oprends)
#    A=int(A)
#    B=int(B)
#    if oprends == '+':
#       print(A+B)
#    elif oprends == '-':
#       print(A-B)
#    elif oprends == '*':
#       print(A*B)
#    elif oprends == '/':
#       print(A // B)
#       break
if '+' in exp:
    A,B=exp.split('+')
    print(int(A)+int(B))
elif '-' in exp:
   A ,B=exp.split('-')
   print(int(A)-int(B))
elif '*' in exp:
   A ,B=exp.split('*')
   print(int(A)*int(B))
elif '/' in exp:
   A ,B=exp.split('/')
   print(int(A)//int(B))   
  

