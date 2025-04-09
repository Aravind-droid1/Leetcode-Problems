#the problem is to find the maximum of the addition between the sequence of subarrays

class Solution(object):
    def maxSubArray(self, n):
        #here we are assigning value thrug list because if we assign 0 as intial it would neglect the negative value if program started
        max=n[0]
        current=n[0]
        #starting the loop from second value of the list one has been given to current and  max already
        for i in range(1,len(n)):
            if(current+n[i] > n[i]):
                current=current+n[i]
            else:
                current=n[i] 
            if (current > max):
                max=current
        return max    
    
s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
