class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0

        for l in t:
            if s_i < len(s) and l == s[s_i]:
                s_i += 1
            if s_i == len(s):
                return True
            
        return False
        

        