# brute 
def reversearray(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr


arr=[1,2,3,4,5]
print(reversearray(arr))


# optimal
def reversearray(arr):
    return arr[::-1]


arr=[1,2,3,4,5]
print(reversearray(arr))
