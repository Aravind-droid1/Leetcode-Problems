class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        len1 = len(word1)
        len2 = len(word2)
        i, j = 0, 0
        while i < len1 and j < len2:
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len1:
            merged += word1[i:]
        if j < len2:
            merged += word2[j:]
        return merged