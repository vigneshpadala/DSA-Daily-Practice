#Count Even Numbers in Window

#Given an array and integer k,
#count how many even numbers are present in each window of size k.

def count_even(arr,k):
    n=len(arr)
    result=[]
    c_even=0
    for i in range(k):
        if arr[i]%2==0:
            c_even+=1
            
    result.append(c_even)
    for i in range(k,n):
        if arr[i-k]%2==0:
            c_even-=1
    
        if arr[i]%2==0:
            c_even+=1
        result.append(c_even)
    return result
    
arr=[2,1,4,6,3]
k=3
print(count_even(arr,k))
