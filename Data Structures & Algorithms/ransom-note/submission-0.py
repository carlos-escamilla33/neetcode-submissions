class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht = {}

        for l in magazine:
            if l not in ht:
                ht[l] = 0
            ht[l] += 1

        for l in ransomNote:
            if l in ht:
                ht[l] -= 1
                if ht[l] <= 0:
                    del ht[l]
            else:
                return False

        return True
