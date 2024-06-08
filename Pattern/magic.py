# 1.....1
# .2...2.
# ..3.3..
# ...4...
# .2...2.
# 1.....1
n=8
for i in range(1,n):
    for j in range(1,n):
        if i==j or i+j==n:
            print(i,end='')
        else:
            print(' ',end='')
    print()
