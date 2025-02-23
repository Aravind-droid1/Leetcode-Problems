#136 single number
#where we have to find a number which is not repeated in the given array
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in nums:
            result^=i
        return result

nums=[4,2,1,2,1]
obj=Solution()
print(obj.singleNumber(nums))