# Sliding Window is used when the problem asks about:

# Subarray / Substring

# Contiguous elements

# Maximum / Minimum / Count / Sum within a range

# Instead of recalculating again and again (❌ O(n3)),
# we slide a window over the array/string (✅ O(n)).

# -TYPES OF SLIDING WINDOW:

# 1️⃣Fixed Size Sliding Window
# Window size = constant (k)
# Example: Maximum Sum Subarray of Size k

# 2️⃣ Variable Size Sliding Window
# Window size changes based on condition.
# Example: Smallest Subarray with Sum ≥ S


# BIG O NOTATION (❌ O(N3))
---

li=[5,9,1,8,7,5,3]
n=len(li)
ans=0
l=5
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(li[k])
            tsum+=li[k]
        if len(temp)==l:
            print(temp,tsum)
            ans=max(ans,tsum)
print(ans)

# BIG O NOTATION (✅ O(n)).

li=[5,9,1,8,7]
n=len(li)
l=0
temp=0
k=3
ans=0
for r in range(n):
    temp+=li[r]

    if(r-l==k):
        temp-=li[l]
        l+=1
        
    if(r-l+1==k):
        ans=max(ans,temp)
print(ans)
