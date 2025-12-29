#To Check if an Array Element is in a HashMap

def hash_map(arr,freq):
    for i in arr:
        freq[i]=freq.get(i,0)+1
    target=3
    if target in freq:
        print("present")
    else:
        print("not present")
    return freq
arr=[1,3,1,2,3,1,2]
freq={}
print(f"elements stored in array:{hash_map(arr,freq)}")
