#Count Vowels in a String

def count_vowel(s):
    vowel='aeiouAEIOU'
    count=0
    for ch in s:
        if ch in vowel:
            count+=1
    return count

s="vigneshpatel"
print(count_vowel(s))
