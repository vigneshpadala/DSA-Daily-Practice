def brute(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]  :
            return "Array not sorted"
    return "Array  sorted" 

def optimal(arr):
    return all(arr[i]<arr[i+1] for i in range(len(arr)-1))
    
arr=[1,4,6,7,8,10]
print(brute(arr))
print(optimal(arr))
