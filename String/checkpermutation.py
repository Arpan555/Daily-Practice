str1='string'
str2='stirgns'
def checkPerm(str1, str2):
    a=sorted(str1)
    st1 = ''.join(a)
    b=sorted(str2)
    st2 = ''.join(b)
    if st1 == st2:
        return True
    else:
        return False
print(checkPerm(str1,str2))