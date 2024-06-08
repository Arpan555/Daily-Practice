# 1
# 11
# 202
# 3003
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1:
            print('1', end=' ')
        elif j==1 or i==j:
            print(i-1,end=" ")
        else:
            print('0',end=' ')
    print()