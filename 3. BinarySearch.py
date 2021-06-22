from array import*
a=array('i',[])

def binarySearch(a, val):
    lb=0
    ub=len(a)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if a[mid]== val:
            return mid
        elif a[mid]>val:
            ub=mid-1
        elif a[mid]<val:
            lb=mid+1
    return -1

arr=array('i',[])
n=int(input('Enter array size: ',))
print('Enter',n,'sorted array elements')
for i in range(n):
    x=int(input())
    arr.append(x)
v=int(input('Enter the value to be searched: '))

pos=binarySearch(arr,v)
if pos!=-1:
    print('position of',v,'is:',pos)
else:
    print('Value not found')
