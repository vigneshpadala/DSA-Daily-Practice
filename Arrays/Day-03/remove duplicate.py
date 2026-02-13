# Brute
def removeduplicate(arr):
    unq=[]
    for num in arr:
        if num  not in unq:
            unq.append(num)
        else:
            num+=1
    return unq

arr=[1,2,2,3,3,4,4,5]
print(removeduplicate(arr))

