# 1480. Running Sum of 1d Array

class Solution(object):
    def runningSum(self, nums):
        total=0
        result=[]
        for i in range(len(nums)):
            total+=nums[i]
            result.append(total)
        return result
        
