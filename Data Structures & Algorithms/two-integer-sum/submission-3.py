class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in ht:
                return [min(ht[x], i), max(ht[x], i)]
            else:
                ht[nums[i]] = i