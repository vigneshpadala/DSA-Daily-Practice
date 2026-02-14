#  Rotate an array by k positions
# brute - O(n*(k%n))
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

# optimal- O(n)
def optimal(arr,k):
    k = k % len(arr)
    print(f'k={k},arr[-k:]={arr[-k:]},arr[:-k]={arr[:-k]}')
    return arr[-k : ] + arr[ : - k] 
        
arr=[1,2,3,4,5]
k=3
print(optimal(arr,k))
