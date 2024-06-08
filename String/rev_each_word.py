str='Welcome to Coding Ninjas'
lst=str.split(' ')
# emocleW ot gnidoC sajniN
op=[]
for i in range(len(lst)):
    op.append(lst[i][::-1])
op=' '.join(op)
print(op)

