# 1111
# 000
# 11
# 0
n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        if i%2==0:
            print('0',end='')
        else:
            print('1',end='')
    print()