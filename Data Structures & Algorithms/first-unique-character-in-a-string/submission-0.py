class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}

        for i in range(len(s)):
            if s[i] not in ht:
                ht[s[i]] = 0
            ht[s[i]] += 1

        for i in range(len(s)):
            if ht[s[i]] == 1:
                return i
        
        return -1




        