# 523. Continuous Subarray Sum

class Solution(object):
    def checkSubarraySum(self, nums, k):
        running_sum = 0
        rem_map = {0: -1}

        for i, num in enumerate(nums):
            running_sum += num
            rem = running_sum % k

            if rem not in rem_map:
                rem_map[rem] = i

            elif i - rem_map[rem] >= 2:
                return True

        return False
