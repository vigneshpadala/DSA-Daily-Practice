# brute
def majorityElement(arr):
    for x in set(arr):
        if arr.count(x) > len(arr) // 2:
            return x

arr=[3,2,3,3,2,2,1,1,1,1]
print(majorityElement(arr))

# optimal
