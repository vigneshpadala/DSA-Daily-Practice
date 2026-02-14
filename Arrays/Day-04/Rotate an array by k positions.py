#  Rotate an array by k positions
def brute(arr,k):
    n=len(arr)
    rotations= k % n
    for i in range(rotations):
        last_ele = arr.pop()
        arr.insert(0,last_ele)
    return arr
    
    
arr=[1,2,3,4,5]
k=2
print(brute(arr,k))
