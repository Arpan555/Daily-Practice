def tripplet(arr,x):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==x:
                    c+=1
    return c

arr=[1, 2, 3, 4, 5, 6, 7]
x=12
print(tripplet(arr,x))