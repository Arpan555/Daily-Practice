str='abcad'
op=[0]*256
max=-1
c=''
for i in str:
    op[ord(i)]+=1
for i in str:
    print(op[ord(i)])
    if max < op[ord(i)]:
        max = op[ord(i)]
        c=i
print(c)