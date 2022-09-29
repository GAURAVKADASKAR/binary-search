''' binary search'''
def binary_search(a,n):
    low=0
    high=len(a)-1
    mid=0
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]>n):
            high=mid-1
        elif(a[mid]<n):
            low=mid+1
        else:
            return mid
    return -1
a=[1,2,3,4,5]
n=4
re=binary_search(a, n)
if(re==0):
    print("number is founded")
else:
    print("number is founded at position",str(re))
        