# 1984. Minimum Difference Between Highest and Lowest of K Scores

class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        n=len(nums)
        l=0
        ans=float("inf") 
        for r in range(n):
            if r-l==k:
                l+=1

            if r-l+1==k:
                ans=min(ans,nums[r]-nums[l])
        return ans
