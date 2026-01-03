#290. Word Pattern
#link:https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word
            
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch
        
        return True
