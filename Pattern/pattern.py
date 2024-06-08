# ...1
# ..121
# .12321
# 1234321
# .12321
# ..121
# ...1

n=5
m=n//2+1
i=1
for i in range(1,n):
    for space in range(n-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(2,i+1):
        print(i-k+1,end='')
    print()
for i in range(1,m+1):
    for space in range(1+i):
        print(" ",end='')
    for j in range(i,m+1):
        print(j-i+1,end='')
    for k in range(i,m):
        print(k+1-i,end='')
    print()
    