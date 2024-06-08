def selection_sort(arr,size):
    for i in range(size-1):
        min=i
        for j in range(i+1,size):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
input=[4,5,1]
selection_sort(input,len(input))
print(input)