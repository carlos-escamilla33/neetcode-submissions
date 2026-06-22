import copy

class Solution:
    def helper(self, copy, word):
        for char in word:
            if char in copy and copy[char] > 0:
                copy[char] -= 1
            else:
                return False
        
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}

        for char in chars:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        res = 0

        for word in words:
            if self.helper(copy.deepcopy(count), word):
                res += len(word)
        
        return res


"""
Goal: we want to find the total length of the word(s) that are in chars


"""
        