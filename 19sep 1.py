# sentence = "I am a good girl"
# count =0
# word = ""
# for ch in sentence + " ":
#     if ch!= " ":
#         word+= ch
#     else:
#         if word != " ":
#             count+=1
#             word = "" 
# print(f"the sentence has{count} words")                


# armstrong number check

num=153
power = len(str(num))
total=0
for digits in str(num):
    total+= int (digits)**power
print(num, " is armstrong?" , total == num)