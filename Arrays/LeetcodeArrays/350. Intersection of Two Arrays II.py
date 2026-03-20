class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i=j=0
        new_arr=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                new_arr.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return new_arr
