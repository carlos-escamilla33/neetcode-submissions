class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        min_appearances = len(nums) // 3

        res = []

        for num in num_count:
            if num_count[num] > min_appearances:
                res.append(num)

        return res