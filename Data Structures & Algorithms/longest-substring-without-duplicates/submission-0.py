class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        longest_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in chars_set:
                chars_set.remove(s[left])
                left += 1
            chars_set.add(s[right])
            longest_length = max(longest_length, (right - left) + 1)
        
        return longest_length

"""
create a set holding non-dups
create length variable
iterate through the string:
    while the current character is in the set:
        shorten the left side
        remove the character
    take the max from the length variable and the (l+r)

return the length variable
"""
        