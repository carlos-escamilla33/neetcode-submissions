class Solution:
    def scoreOfString(self, s: str) -> int:
        currSum = 0
        left = 0

        for right in range(1, len(s)):
            currSum += abs(ord(s[left]) - ord(s[right]))
            left += 1
        
        return currSum
        