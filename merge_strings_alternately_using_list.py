class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        merged = []
        len1, len2 = len(word1), len(word2)
        i, j = 0, 0
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1; j += 1
        if i < len1:
            merged.append(word1[i:])
        elif j < len2:
            merged.append(word2[j:])
        return ''.join(merged)
