class Solution(object):
    def shuffle(self, nums, n):
        #create an array named arr
        arr = []
        for i in range (n):
            #now there are two appendings are going on 1.(i) 2.(n+i) into the arr array
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr