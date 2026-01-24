#560. Subarray Sum Equals K

class Solution(object):
    def subarraySum(self, nums, k):
        running_sum=0
        count=0
        map1={0:1}
        for num in nums:
            running_sum+=num
            if running_sum-k in map1:
                count+=map1[running_sum-k]
            freq[running_sum] = freq.get(running_sum, 0) + 1
        return count
        
