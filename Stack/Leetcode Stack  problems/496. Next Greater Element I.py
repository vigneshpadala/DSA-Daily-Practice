#496. Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for current in nums2:
            while stack and current > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = current
            stack.append(current)

        for x in stack:
            next_greater[x] = -1

        return [next_greater[x] for x in nums1]
