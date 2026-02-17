# Maximum sum of row
def maximum(arr):
    max_sum=float("-inf")
    max_ind=-1
    for i in range(len(arr)):
        row_sum=sum(arr[i])
        if row_sum>max_sum:
            max_sum=row_sum
            max_ind=i
    print("max sum:",max_sum)
    print("row:",max_ind)
    
    
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(maximum(arr))

# one line code 
def maximum(arr):
    max_sum,max_ind=max(enumerate(map(sum,arr)))
    print("max sum:",max_sum)
    print("row:",max_ind)
    
    
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(maximum(arr))
