class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        currLen = 0

        for num in nums:
            if num == 1:
                currLen += 1
            else:
                currLen = 0
            maxLen = max(currLen, maxLen)

        return maxLen


        