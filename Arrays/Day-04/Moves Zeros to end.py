# brute
def brute(arr):
    count=0
    s=[]
    for i in arr:
        if i!=0:
            s.append(i)
        else:
            count+=1
    for i in range(count):
        s.append(0)
    return s
    
arr=[1,0,2,0,3,4,5]
print(brute(arr))

# optimal
def optimal(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        if arr[l]!=0:
            l+=1
        else:
            arr[l],arr[r]=arr[r],arr[l]
            r-=1
    return arr
    
arr=[1,0,2,0,3,4,5,0,0,0]
print(optimal(arr))
