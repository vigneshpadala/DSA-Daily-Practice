# Brute - O(n2)
def removeduplicate(arr):
    unq=[]
    for num in arr:
        if num  not in unq:
            unq.append(num)
    return unq

arr=[1,2,2,3,3,4,4,5]
print(removeduplicate(arr))

# optimal - O(n)
def removeduplicate(arr):
    return list(set(arr))

arr=[1,2,2,3,3,4,4,5]
print(removeduplicate(arr))
