# Пункт1

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# Find out if a,b,c makes the Pythagorean triplet
if a <= b <= c and c**2 == (a**2)+(b**2):
    print("Makes the Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")

# пункт 2

user_num = int(input('Enter positive integer:'))
output = 0
while user_num != 0:
    a = user_num % 10
    output = 10 * output + a
    user_num //= 10
print(output)

user_str = int(input('Enter positive integer:'))
str1 = str(user_str)
str2 = str1[::-1]
print(str2)
