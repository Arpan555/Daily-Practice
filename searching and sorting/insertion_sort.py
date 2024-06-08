def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp =arr[i]
        while (j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=temp
arr=[6,4,1,2]
insertionSort(arr)
print(arr)