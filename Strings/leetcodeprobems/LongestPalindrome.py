#409.find the maximum length of a palindrome that can be built using the characters of s
link: https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s):
        charFrequency = Counter(s)  #Counter(s) counts how many times each character appears  Counter(s) → {'c': 4, 'd': 2, 'a': 1, 'b': 1}
        oddFrequencyCount = 0
        for frequency in charFrequency.values():
            if frequency % 2 == 1:   #Loop through all character frequencies
                oddFrequencyCount += 1  #If frequency is odd, increment oddFrequencyCount
        if oddFrequencyCount > 1:
            return len(s) - oddFrequencyCount + 1
        return len(s)
