#1844. Replace All Digits with Characters
#You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
#You must perform an operation shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        for i in range(len(s)):
            if i%2 != 0:
                #we are recording the even numbered index value being changed from char to ascii value
                r=ord(s[i-1])
                #then add them into the integer changed value and then again change them into 
                s[i]=chr(int(s[i])+r)
        return "".join(s)
obj=Solution()
print(obj.replaceDigits("a1c1e1f1"))
print(obj.replaceDigits("a1b2c3d4e"))
print(obj.replaceDigits("v0h2x1p4"))