class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = [[] for idx in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        for idx in range(len(buckets) - 1, 0, -1):
            for num in buckets[idx]:
                res.append(num)
                if len(res) == k:
                    return res

        