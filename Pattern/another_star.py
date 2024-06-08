# ...1
# ..232
# .34543
# 4567654
n=4
i=1
while i<=n:
    sp=1
    while sp<=n-i:
        print(" ",end='')
        sp+=1
    j=1
    p=i
    while j<=i:
        print(p,end='')
        p+=1
        j+=1
    q=2*i-1
    while q>i:
        q-=1
        print(q,end='')
    print()
    i+=1
    