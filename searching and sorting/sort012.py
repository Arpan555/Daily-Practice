arr=[2,0,1,1,0,2,1,0,1,2]
n=len(arr)
init_zero = 0
init_two = n-1
i=0
while i <= init_two:
    if arr[i]==0:
        temp = arr[init_zero]
        arr[init_zero]=arr[i]
        arr[i]=temp
        i+=1
        init_zero+1
    elif arr[i]==2:
        temp=arr[init_two]
        arr[init_two]=arr[i]
        arr[i]=temp
        init_two-=1
    else:
        i+=1
print(arr)