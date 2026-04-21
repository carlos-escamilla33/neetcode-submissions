import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        max_heap = []

        for num in freq:
            heapq.heappush(max_heap, (-freq[num], num))
        
        res = []
        for i in range(k):
            neg_freq, val = heapq.heappop(max_heap)
            res.append(val)
        
        return res
        