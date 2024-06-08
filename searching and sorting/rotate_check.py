# like if we have arr [4, 5, 6, 1, 2, 3] then op is 3 becuase first come 6 in front then 5 and 4 so total is 3
arr=[4,5,6,11,12,13]


def rotate_check(arr):
    n=len(arr)
    for i in range(1,n-1):
        if arr[i]>arr[i+1]:
            return i+1
    
    return 0
print(rotate_check(arr))