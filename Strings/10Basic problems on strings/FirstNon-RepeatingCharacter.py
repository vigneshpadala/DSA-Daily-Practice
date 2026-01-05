#First Non-Repeating Character

from collections import Counter
def first_not_repeatingchar(s):
    count=Counter(s)
    for ch in s:
        if count[ch]==1:
            return ch

s="viggi"
print(first_not_repeatingchar(s))
