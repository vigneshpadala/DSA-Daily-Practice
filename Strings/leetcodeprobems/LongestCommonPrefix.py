#14. Longest Common Prefix
link:https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
