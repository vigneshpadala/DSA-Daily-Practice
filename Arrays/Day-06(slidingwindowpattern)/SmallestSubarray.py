#find Smallest Subarray
def smaller_subarry(arr, k):
    left=0
    window_sum=0
    min_len=0
    for right in range(len(arr)):
        window_sum+=arr[right]
        if window_sum>=k:
            window_sum-=arr[left]
            left+=1
        min_len=max(min_len,left)
    return min_len
arr=[2,1,4,6,3]
k=10
print(smaller_subarry(arr,k))
