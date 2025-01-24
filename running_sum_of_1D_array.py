class Solution(object):
    def runningSum(self, nums):
        n = 0
        #create a array
        arr=[]
        #in each iterations the n keeps on add up the value with the previous ones all and appens in arr as a new value
        for i in nums:
            n = n + i
            arr.append(n)
        return arr