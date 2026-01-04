# What is an Anagram?

# Two strings are called anagrams if:

# They contain the same characters
# With the same frequency
# But possibly in a different order

# | String 1 | String 2 | Anagram? |
# | -------- | -------- | -------- |
# | listen   | silent   | Yes      |
# | race     | care     | Yes      |
# | hello    | world    | No       |
# | aacc     | ccac     | No       |


def is_anagram(s1,s2):
    return sorted(s1) == sorted(s2)
  
s1="silent"
s2="listen"
print(is_anagram(s1,s2))
