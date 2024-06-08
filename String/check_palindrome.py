def palindrom(str):
    if str==str[::-1]:
        return True
    else:
        return False
str='abcccvcba'
print(palindrom(str))
