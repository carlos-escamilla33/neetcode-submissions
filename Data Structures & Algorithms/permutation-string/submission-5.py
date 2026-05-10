class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        window = {}
        k = len(s1)

        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            if right >= k:
                left_char = s2[right - k]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            if right >= k - 1:
                if window == s1_count:
                    return True

        return False


"""
Goal: Attempt to find the the string s1 in s2, even if the letters are scrambled,

Do the letters in a permuation have to be together? 
- Yes, they do

- We need to return false if s1 is of a greater length than s2

Will both inputs always be valid?
- Yes, both will have a length of at least 1 or greater but less than or equal to 1000
"""
