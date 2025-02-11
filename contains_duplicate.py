#217.contains duplicate
#to find if the number is repeated in an array or not
class Solution(object):
    def containsDuplicate(self, nums):
        l=len(nums)
        #checks if length of num is lesser than or equal to one if it is we cant find duplicate so it exits
        if (l<=1):
            return False
        nums.sort()
        #to check till last we are taking range length-1 so i can stop befare last one then i+1 can reach till last
        for i in range(l-1):
            if(nums[i]==nums[i+1]):
                return True
        return False
       
obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
print(obj.containsDuplicate([1,2,3,4]))
print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(obj.containsDuplicate([1]))