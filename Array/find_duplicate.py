def findDuplicate(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                break
    return arr[i]
    
arr=[1,4,5,5]
print(findDuplicate(arr,len(arr)))