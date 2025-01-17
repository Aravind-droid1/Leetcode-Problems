class Solution(object):
    def reverseString(self, s):
        # Get the length of the list
        n = len(s)
        
        # Iterate only through the first half of the list
        for i in range(n // 2):
            # Swap the elements at position i and n - i - 1
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
