class Solution:
    def maxCount(self, ht):
        currMaxCount = 0

        for char in ht:
            if ht[char] > currMaxCount:
                currMaxCount = ht[char]

        return currMaxCount
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        window_size = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1
            while (((right - left) + 1) - (self.maxCount(count))) > k:
                count[s[left]] -= 1
                left += 1
            window_size = max(window_size, (right - left) + 1)
        
        return window_size

    

"""
Goal: return the length of the longest substring that contains one type of char

What if k is zero?
- k can be zero, no replacements are needed / available
What if s is empty?
- 

get the character that has the max count and then build a string around it



"""