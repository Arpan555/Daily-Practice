# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
n=5
i=1
while i <=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    sp=1
    while sp<=((2*n)-(2*i)):
        print(" ",end='')
        sp+=1
    p=i
    j=1
    while j<=i:
        print(p,end='')
        p-=1
        j+=1
    print()
    i+=1
