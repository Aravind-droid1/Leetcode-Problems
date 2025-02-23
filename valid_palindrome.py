#125 valid palindrome
#to check if the palindrome is correct or not even with the space being cut down only with numbers and characters
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #changes to lower case but wont change the digits
        s=s.lower()
        r=""
        for i in s:
            #the s is in string
            if (ord('0') <= ord(i) <= ord('9'))or(97 <= ord(i) <= 122):
                r=r+i
        l=len(r)
        left, right = 0, len(r) - 1
        while left < right:
            if r[left] != r[right]:
                return False
            left += 1
            right -= 1
        return True
    
sol = Solution()
print(sol.isPalindrome("12321"))
print(sol.isPalindrome("123321"))
print(sol.isPalindrome("123421"))
print(sol.isPalindrome("A1b2B1a"))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome("race a car"))