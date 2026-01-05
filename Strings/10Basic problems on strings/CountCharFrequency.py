#Count Character Frequency
#1.Dictonary
#2.Counter method

def count_char_frequency(s):
    freq={}
    for char in s:
            freq[char]=freq.get(char,0)+1
    return freq

s="viggi"
print(count_char_frequency(s))
