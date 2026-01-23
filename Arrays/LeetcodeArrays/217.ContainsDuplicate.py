# 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        seen={}
        for i,nums in enumerate(nums):
            if nums in seen:
                return True
            seen[nums]=i
        return False
