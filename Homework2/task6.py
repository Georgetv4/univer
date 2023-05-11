def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i+1]) - ord(chars[i]) > 1:
            return print('The missing letter is:', chr(ord(chars[i]) + 1))
    else:
        return "There is no missing letters"


find_missing_letter('abcefg')
