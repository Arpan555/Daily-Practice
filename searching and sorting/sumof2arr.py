arr1 = [6,2,4]
arr2 = [7,5,6]
 
size=max(1+len(arr1),len(arr2))
op=[0]*size
def sum2arr(arr1,arr2,op):
    m=len(arr1)
    n=len(arr2)
    i=m-1
    j=n-1
    carry=0
    k= max(m,n)
    while i>=0 and j>=0:
        sum = arr1[i]+arr2[j]+carry
        op[k]= sum%10
        carry = sum //10
        i-=1
        j-=1
        k-=1
    while i>=0:
        sum = arr1[i]+carry
        op[k]= sum%10
        carry = sum //10
        i-=1
        k-=1
    while j>=0:
        sum = arr2[j]+carry
        op[k]= sum%10
        carry = sum //10
        j-=1
        k-=1
    op[0]=carry
sum2arr(arr1,arr2,op)
print(op)