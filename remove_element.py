#Question
#Given an integer array nums and an integer val, write a function to remove all occurrences of val in the array in-place.
#The order of the remaining elements in the array may be changed. 
#After removing all occurrences of val, return the number of elements in the array that are not equal to val.

class Solution(object):
    def removeElement(self, nums, val):
        # Initialize the variable k to count the number of elements not equal to val
        k = 0
        # Initialize i to track the current index in the list
        i = 0
        
        # Iterate through the list as long as i is within the bounds of the list
        while i < len(nums):
            # If the current element equals the value we want to remove
            if nums[i] == val:
                # Remove the element at index i using pop
                nums.pop(i)
                # We don't increment i here because pop shifts elements to the left
            else:
                # If the element is not equal to val, increment i and count this element
                i += 1
                k += 1
        
        # Return the number of elements in nums that are not equal to val
        return k
