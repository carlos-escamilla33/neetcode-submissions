class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_ht = {}

        for l in s:
            if l not in s_ht:
                s_ht[l] = 0
            s_ht[l] += 1
        
        for l in t:
            if l not in s_ht:
                s_ht[l] = 1
            
            if l in s_ht:
                s_ht[l] -= 1
                if s_ht[l] == 0:
                    del s_ht[l]
        
        return len(s_ht) == 0
        




"""
goal: find if s and t are anagrams of eachother

- what do we return if one string is empty?
- if they dont match we return false?
- its not enough for all the letters to match, we need the same freq
- they need to be the same length

ex: 
    t = bob s = bbo, true because all letters and freq match
ex:
    t = aa, s = a
edgecase:
    t = "", s = "hello"

- this is a hashtable problem
- freq counter problem

we need to get the length of each and compare before continuing 
    if they dont match we return false

create a freq table of the first string

iterate over the second string
    if the character is in the hashtable
"""