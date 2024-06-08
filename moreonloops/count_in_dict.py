a='qwertyuiopadhjfgghfgfd'
dict={}
for i in a:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]+=1
print(dict)