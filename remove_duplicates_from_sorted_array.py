# 26. Remove Duplicates from Sorted Array
#Write a Python function removeDuplicates that takes a sorted list of integers, nums.
#And removes the duplicate elements in place such that each unique element appears only once. 
#The function should return the new length of the list containing only unique elements.

class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize a pointer `i` to track the current index in the list
        i = 0
        
        # Loop through the list while `i` is less than the second-to-last index
        while i < len(nums) - 1:
            # If the current element is the same as the next element, it's a duplicate
            if nums[i] == nums[i + 1]:
                # Remove the duplicate by popping the next element
                nums.pop(i + 1)
            else:
                # If no duplicate is found, move to the next index
                i += 1
        
        # After processing, the length of the list represents the count of unique elements
        k = len(nums)
        return k  # Return the count of unique elements
