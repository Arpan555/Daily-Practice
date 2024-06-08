def findUnique(arr,n):
    for i in range(n):
        j=0
        while j<n:
            if i != j:
                if arr[i] == arr[j]:
                    break
            j+=1
        if j==n:
            return arr[i]
arr=[1,2,3,4,5,6,7,6,5,4,3,2,1]
print(findUnique(arr,len(arr)))