#Find maximum subarray sum when all numbers are negative.

def kadane(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        curr_sum=max(curr_sum,arr[i])
        max_sum=max(max_sum,curr_sum)
    return (max_sum)

arr=[-2,-3,-1,-4,-7,-1,-3,-6,-8,-10]
print(kadane(arr))
