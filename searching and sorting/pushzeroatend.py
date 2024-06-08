def pushzeroatend(arr,n):
    count=0
    for i in range(n):
        if arr[i] != 0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
arr=[1,2,3,0,3,3,0,0]
pushzeroatend(arr,len(arr))
print(arr)
