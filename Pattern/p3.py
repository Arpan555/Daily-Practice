# 1234
# 123
# 12
# 1

n=5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(j,end=' ')
    print()

n=4
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i+1-j,end=' ')
    print()