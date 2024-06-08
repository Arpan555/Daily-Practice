str='abcabcaabbcc'

def removeConsecutiveDuplicates(string) :
    chars = []
    prev = None
    for c in string:
        if prev != c:
            chars.append(c)
            prev = c
 
    return ''.join(chars)
print(removeConsecutiveDuplicates(str))