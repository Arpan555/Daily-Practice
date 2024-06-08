def pairSum(arr):
    sum=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                sum+=arr[i]+arr[j]
    return sum

arr=[1,2,3,4,3,5,6,7,8]
print(pairSum(arr))