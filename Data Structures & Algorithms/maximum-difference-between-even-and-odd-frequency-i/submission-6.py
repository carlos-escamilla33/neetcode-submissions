class Solution:
    def maxDifference(self, s: str) -> int:
        char_count = {}
        even_min_freq = float("inf")
        odd_max_freq = float("-inf")

        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

        for char in char_count:
            if char_count[char] % 2 == 0:
                even_min_freq = min(even_min_freq, char_count[char])
            else:
                odd_max_freq = max(odd_max_freq, char_count[char])

        return odd_max_freq - even_min_freq