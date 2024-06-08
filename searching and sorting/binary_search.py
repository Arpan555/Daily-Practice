def binarySearch(arr,x):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7,8,9,34,37,43,455]
res=binarySearch(arr,7)
print(res)
