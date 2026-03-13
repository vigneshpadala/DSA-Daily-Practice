class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        nums_set=set(nums)
        l=1
        for num in nums_set:
            if num-1 not in nums_set:
                curr=num
                c_l=1
                while curr+1 in nums_set:
                    curr+=1
                    c_l+=1
                l=max(l,c_l)
        return l
