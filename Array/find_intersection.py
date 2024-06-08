def intersection(arr1, n, arr2, m):
    common=[]
    ran=m if m>n else n
    for i in range(ran):
        if ran==m:
            if arr2[i] in arr1:
                common.append(arr2[i])
        else:
            if arr1[i] in arr2:
                common.append(arr1[i])
    return common


arr1 = [1,2,3,4,5]
arr2 = [5,6,7,4,8,9]
print(intersection(arr1, len(arr1), arr2, len(arr2)))