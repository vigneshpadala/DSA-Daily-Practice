# brute
def majorityElement(arr):
    for x in set(arr):
        if arr.count(x) > len(arr) // 2:
            return x

arr=[3,2,3]
print(majorityElement(arr))

# optimal
def majorityElement(arr):
    count=0
    x=None
    for num in arr:
        if count ==0:
            x=num
        if num==x:
           count+=1
        else:
            count-=1
    return x

arr=[3,2,3]
print(majorityElement(arr))
