def sort01(arr):
    c = arr.count(0)
    for i in range(len(arr)):
        if i<c:
            arr[i]=0
        else:
            arr[i]=1
    return arr
            


arr=[1,1,1,0,1,0]
print(sort01(arr))