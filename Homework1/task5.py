user_input = str(input())
finish = False
if len(user_input) != 0:
    for i in user_input:
        if user_input.lower().count(i.lower()) == 1:
            print(i)
            finish = True
            break
    if finish is not True:
        print("Error! There are no characters in the string that occur once!")
else:
    print("Error! There are no characters in the string that occur once!")
