def binary_search(arr,x,low,high):
    mid = low
    index = -1
    while low<high:
        mid = low+(high-low)//2
        if arr[mid]>x:
            high=mid
        elif arr[mid]<x:
            low=mid+1
        else:
            index=mid
            high=mid
    
    return index
arr=[1,2,4,4,5,5,6,6,7,7,8,8]
print(binary_search(arr,8,0,len(arr)-1))