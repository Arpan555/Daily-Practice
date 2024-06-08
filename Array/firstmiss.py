def firstMissing(arr, n):
    # Write your function here.
    for i in range(1,n+2):
        if i not in arr:
            return i
    else:
        return 1
arr=[26 ,-18 ,34 ,22 ,31 ,3 ,5 ,23 ,-40, -10]
print(firstMissing(arr,len(arr)))