#Two pointer
#opposite direction

#reverse Array
arr=[1,2,3,4,5,6,7,8,9]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)

#check palindrome or not
def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l< r:
        if s[l]!=s[r]:
            return False
        l+= 1
        r-= 1
    return True
# Test
print(is_palindrome("madam"))     # True
print(is_palindrome("hello"))     # False

#pair of sum
def pair_sum(l1, target) -> bool:
    l1.sort()          # Step 1: sort the list
    f = 0
    b = len(l1) - 1
    while f < b:
        curr_sum = l1[f] + l1[b]
        if curr_sum == target:
            return True
        elif curr_sum > target:
            b -= 1
        else:
            f += 1
    return False       # Step 3: if no pair found
l1 = [2, 6, 3, 7, 1]
target = 5
print(pair_sum(l1, target))
