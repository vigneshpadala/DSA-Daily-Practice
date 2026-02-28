# 2586. Count the Number of Vowel Strings in Range
class Solution(object):
    def vowelStrings(self, words, left, right):
        c=0
        v={'a', 'e', 'i', 'o','u'}
        for i in range(left,right+1):
            w=words[i]
            if w[0] in v and w[-1] in v:
                c+=1
        return c
