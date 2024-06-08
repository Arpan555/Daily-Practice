def merge2arr(a1,a2):
    i,j=0,0
    len1,len2=len(a1),len(a2)
    new_arr=[]
    while (i < len1 and j < len2):
        if a1[i] < a2[j]:
            new_arr.append(a1[i])
            i+=1
        else:
            new_arr.append(a2[j])
            j+=1
    while (i<len1):
        new_arr.append(a1[i])
        i+=1
    while (j<len2):
        new_arr.append(a2[j])
        j+=1
    return new_arr
a1=[4,9,18]
a2=[1,2,7,8,9]
print(merge2arr(a1,a2))
