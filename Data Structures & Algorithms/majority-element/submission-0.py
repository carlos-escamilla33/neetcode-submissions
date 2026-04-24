class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        currMajElm = 0
        currMax = 0

        for num in nums:
            if num not in ht:
                ht[num] = 0
            ht[num] += 1

            if ht[num] > currMax:
                currMajElm = num
                currMax = ht[num]

        return currMajElm 


            
        