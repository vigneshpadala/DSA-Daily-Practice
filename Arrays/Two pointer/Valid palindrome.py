def Valid_Palindrome(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        if arr[l]!=arr[r]:
            return False
        else:
            l+=1
            r-=1
    return True
            
arr = "abababa"
print(Valid_Palindrome(arr))
