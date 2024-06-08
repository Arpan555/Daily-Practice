num=371
n=len(str(num))
rev=0
temp=num
while num>0:
    r=num%10
    rev=rev+r**n
    num=num//10
if rev==temp:
    print('Armstrong number')
else:
    print('Not Armstrong')