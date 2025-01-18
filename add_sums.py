#Question
"""Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
You may assume that each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

class Solution(object):
    def twoSum(self, nums, target):
        # Get the length of the input list
        l = len(nums)
        
        # Outer loop: iterate through each element in the list
        for i in range(l):
            # Inner loop: iterate through the elements that come after the current element in the outer loop
            for j in range(i + 1, l):
                # Check if the sum of the two elements equals the target
                if nums[i] + nums[j] == target:
                    # If a pair is found, return their indices as a list
                    return [i, j]
