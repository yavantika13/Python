text= "234"
is_pailndrome = True
for i in range(len(text)//2):
    if text[i] != text[-(i+1)]:
        is_pailndrome = False
        break
    if is_pailndrome:
        print(f"'{text}' is a palindrome")
    else:
         print(f"'{text}' is not a palindrome")
    
