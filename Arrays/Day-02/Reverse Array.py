# brute - 0 (n)
def reversearray(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    return arr

arr=[1,2,3,4,5]
print(reversearray(arr))


# avg - O(log n)
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


# optimal - O(1)
def reversearray(arr):
    return arr[::-1]

arr=[1,2,3,4,5]
print(reversearray(arr))
