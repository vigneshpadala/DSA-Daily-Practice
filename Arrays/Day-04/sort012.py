def sort012(arr):
    c1=0
    c2=0
    c3=0
    
    
    for i in arr:
        if arr[i]==0:
            c1+=1
        elif arr[i]==1:
            c2+=1
        else:
            c3+=1
    idx=0
    for i in range(c1):
        arr[idx]=0
        idx+=1
    for i in range(c2):
        arr[idx]=1
        idx+=1
    for i in range(c3):
        arr[idx]=2
        idx+=1
    
if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    sort012(arr)
    
    for x in arr:
      print(x, end = " ")
