def find_longest(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

def find_smallest(arr):
    max=arr[0]
    for i in arr:
        if i<max:
            max=i
    return max
            
arr=[6,2,9,3,5]
print(f'longest number : {find_longest(arr)}')
print(f'smallest number : {find_smallest(arr)}')
