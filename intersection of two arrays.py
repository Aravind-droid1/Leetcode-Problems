#349.intersection of two arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                nums+=[i]
        return nums

obj=Solution()
print(obj.intersection([1,2,2,2,3],[1,4,5,2]))