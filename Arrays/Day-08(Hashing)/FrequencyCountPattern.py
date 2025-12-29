It means using a hash table (dictionary in Python) to:
Store frequency
Store seen elements
Check existence in O(1) time

📌 Used when problems involve:
Duplicates
Frequency counts
Fast lookups
Complement / difference checks

#hashingFrequency Count Pattern:

def hash_map(arr,freq):
    for i in arr:
        freq[i]=freq.get(i,0)+1
    return freq
arr=[1,3,1,2,3,1,2]
freq={}
print(f"elements stored in array:{hash_map(arr,freq)}")
