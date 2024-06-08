import sys
MIN_VALUE= -2147483648
def sec_largest(arr):
    n=len(arr)
    if n==0:
        return MIN_VALUE
    largest=arr[0]
    s_largest=MIN_VALUE
    for i in range(1,n):
        if largest<arr[i]:
            s_largest=largest
            largest=arr[i]
        elif s_largest<arr[i] and arr[i] != largest:
            s_largest = largest
    return s_largest
arr=[1,2,3,4,5,6,6,4,2,2,1,1,3,4,4]
print(sec_largest(arr))