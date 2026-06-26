class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longestLen = 0

        for num in nums:
            currLen = 0
            while num in nums_set:
                currLen += 1
                num += 1
            longestLen = max(longestLen, currLen)

        return longestLen


"""
    The numbers do not have to be ordered? 
    - No, they do not

    

hashtable problem 
looking up the next available num

store all the values in a hashtable
longestLength = 0

iterate over the nums:
    currLen = 0
    while the next value is in the ht:
        currLen += 1
    max between currLen and longsetLen

return the longestLength

"""
