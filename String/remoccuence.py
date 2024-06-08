str='abc'
x='c'
op=[]
for i in str:
    print(i)
    if i != x:
        print(i)
        op.append(i)
op=''.join(op)
print(op)
