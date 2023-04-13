# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# def find_missing_letter(chars):
#     for i in range(len(chars) - 1):
#         if ord(chars[i+1]) - ord(chars[i]) > 1:
#             return chr(ord(chars[i]) + 1)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if chars.find(chars[i]) - chars.find(chars[i-1]) > 1:
            return alphabet[chars.find(chars[i])]


print(find_missing_letter('abcdfg'))
