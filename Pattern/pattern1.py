# ...1
# ..212
# .32123
# 4321234
n=5
m=n//2+1
for i in range(1,n):
    for sp in range(1,n-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(i+1-j,end='')
    for k in range(2,i+1):
        print(k,end='')
    print()