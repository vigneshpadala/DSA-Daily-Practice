# brute
def brute(arr):
    n=len(arr)
    l=0
    arr.sort()
    for i in arr:
        if i==l:
            l+=1
        else:
            return l
    
arr=[1,0,2,3,5]
print(brute(arr))
