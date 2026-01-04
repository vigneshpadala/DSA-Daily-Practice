#reverse a string using 

# Example:
# Input: "hello" → Output: "olleh"
# Approach:
# Use two pointer or slicing.

#two pointer
def reverse_string(s):
    chars = list(s)      # strings are immutable in Python
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)

print(reverse_string("hello"))

#slicing
def reverse1(s):
    return s[::-1]

s="viggi"
print(reverse1(s))

