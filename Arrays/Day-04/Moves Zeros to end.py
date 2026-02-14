# brute
def brute(arr):
    count=0
    s=[]
    for i in arr:
        if i!=0:
            s.append(i)
        else:
            count+=1
    for i in range(count):
        s.append(0)
    return s
    
arr=[1,0,2,0,3,4,5]
print(brute(arr))

