# 349. Intersection of Two Arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        set1={}
        set2={}
        for i,nums1 in enumerate(nums1):
            if nums1 in set1:
                continue
            set1[nums1]=i
        
        for i,nums2 in enumerate(nums2):
            if nums2 in set1:
                set2[nums2]=i
        return list(set2.keys())
