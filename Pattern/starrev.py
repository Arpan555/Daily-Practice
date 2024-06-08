# ..*
# .***
# *****
# .***
# ..*

n=5
m=n//2+1
for i in range(1,m+1):
    for space in range(m-i):
        print(" ",end='')
    for j in range(2*i-1):
        print("*",end='')
    print()
for i in range(1,m):
    for space in range(i):
        print(" ",end='')
    for j in range(1,n-2*i+1):
        print("*",end='')
    print()
