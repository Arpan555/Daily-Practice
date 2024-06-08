# ...1
# ..12
# .123
# 1234

n=4
i=1
while i<=n:
    sp=1
    while sp<=n-i:
        print(" ", end='')
        sp+=1
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    i+=1
    print()
