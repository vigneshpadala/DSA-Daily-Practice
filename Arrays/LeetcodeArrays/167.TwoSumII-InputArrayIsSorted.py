# 167. Two Sum II - Input Array Is Sorted

class Solution(object):
    def twoSum(self, nums, target):
        l=0
        r=len(nums)-1
        while l<=r:
            sum1=nums[l]+nums[r]
            if sum1==target:
                return [l+1,r+1]
            elif sum1>target:
                r-=1
            else:
                l+=1
