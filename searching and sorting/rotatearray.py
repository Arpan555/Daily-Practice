arr=[1,2,3,4,5,7,6]
d=0
def rotate_array(arr,d):
    arr[:]=arr[d:len(arr)]+arr[0:d]
    return arr
print(rotate_array(arr,d))