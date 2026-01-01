# Traversal Pattern (Strings Basics)
# 📌 Used when:
# Count characters
# Check conditions

#count characters
def str1(ch):
    count = 0
    for i in ch:
        count += 1
    return count
ch="shivakumar"
print(str1(ch))

# Check conditions check wheather palindrome or not using two pointers
def str1(ch) -> bool:
    left = 0
    right = len(ch) - 1
    while left < right:
        if ch[left] != ch[right]:
            return False
        left += 1
        right -= 1
    return True
ch = "shivakumar"
print(str1(ch))
