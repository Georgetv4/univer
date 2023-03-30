# Пункт1
user_str = str(input()).replace(' ', '').lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
longest_str = ''
curr_str = ''
finish = False
for char in user_str:
    if char not in alphabet:
        print("Invalid input! There is character not from alphabet!")
        finish = True

if finish is not True:
    for char in user_str:
        if char not in alphabet:
            print("Invalid input! There is character not from alphabet!")
            break
        if curr_str == '':
            curr_str = char
        elif curr_str[-1] <= char:
            curr_str += char
        elif curr_str[-1] > char:
            if len(longest_str) < len(curr_str):
                longest_str = curr_str
                curr_str = char
            else:
                curr_str = char
    if len(curr_str) > len(longest_str):
        longest_str = curr_str
    print(longest_str)

# Пункт2

user_str = str(input())
user_str.replace(' ', '')
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in user_str:
    if char not in alphabet:
        print("Invalid input! There is character not from alphabet!")
        quit()
if len(user_str) < 3:
    print("Invalid input! There is character not from alphabet")
else:
    print(user_str.count('non'))
