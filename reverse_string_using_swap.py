class Solution(object):
    def reverseString(self, s):
        # Initialize two pointers: one at the beginning (left) and one at the end (right) of the list
        left = 0
        right = len(s) - 1
        
        # Loop until the two pointers meet or cross each other
        while left < right:
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move the left pointer one step to the right
            left += 1
            
            # Move the right pointer one step to the left
            right -= 1