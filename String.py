# myString = 'Hello'
# print(myString)

# #
# myString = "Hello"
# print(myString)

# myString = '''Hello'''
# print(myString)

# myString = "hello"
# print(myString[0])
# print(myString[-1])
# print(myString[2:5])

# #print(myString[7])

# myString = "Hello"
#  #myString[4]= 's'

# del myString

# s1 = "Hello"
# s2 = "Satish"

# #concatenation
# print(s1 + s2)

# # repeat n times
# print(s1 * 3)

#itreate
# count = 0
# for l in "Hello World":
#     if l == 'o':
#         count += 1
# print(count, 'letters found')

#membership op
# print('l' in 'Hello World')
# print('or' in 'Hello World')
# print('hello'.upper())
# #print.lower()

# "this will split all words in a list".split()
# ' '.join(['this', 'will','split', 'all', 'words', 'in', 'a', 'list'])

# "Good Morning".find("Mo")
# print("Good Morning".find("Mo"))

# s1 = "Bad Morning"
# s2 = s1.replace("Bad","Good")
# print(s1)
# print(s2)

#
# myString = "kanak"
# if myString == myString[::-1]:
#         print("string is palindrome")
# else:
#         print("not")

# myString = input("enter a string")
# if myString == myString[::-1]:
#         print("string is palindrome")
# else:
#         print("not")

myStr = " python program to "
words = myStr.split()
words.sort()
for word in words:
        print(word)        