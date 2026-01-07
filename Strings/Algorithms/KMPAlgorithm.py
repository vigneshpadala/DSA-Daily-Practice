#KMP STRING MATCHING ALGORITHM

# What is KMP?
# KMP is a string searching algorithm that finds a pattern in a text in O(n + m) time.
# n = length of text
# m = length of pattern
# 📌 It avoids re-checking characters (unlike brute force).
# -------------------------------------------------------------------------------------------------------
# ✅ KMP Solution Idea
# Use information from the pattern itself to skip comparisons.
# 👉 This info is stored in the LPS array.

# code:
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            print("Pattern found at index", i - j,"->",i)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1



text = "ababcabcabababdc"
pattern = "ababdc"

kmp_search(text, pattern)
