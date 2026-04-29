class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}

        for i in range(len(nums)):
            if nums[i] not in ht:
                ht[nums[i]] = i
            else:
                j = ht[nums[i]]
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                else:
                    ht[nums[i]] = i
        
        return False
        
    
"""
We need to check to see if there are numbers in the array that are equal to each other
and their absolute value is less than or equal to k

example:
    [1,2,3,1], k = 3
    i = 0
    j = 3 abs(0 - 3) = 3 is less than or equal to k

    create a ht

    iterate over the array nums:
        if the array nums is not in ht:
            add it to the ht
        else:
            check to see if the index of the value and the current index are less than 3
                return true if it is
    
    return false the end if not
"""