# checking wheather is palindrome or not

# A string is a palindrome if it reads the same forward and backward.

# Example:
# "madam" → Palindrome
# "hello" → Not a palindrome

def is_palindrome(s):
    return s==s[::-1]

s="madam"
print(is_palindrome(s))
