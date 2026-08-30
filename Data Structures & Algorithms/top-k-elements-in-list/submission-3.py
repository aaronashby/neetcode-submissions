class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            buckets[count].append(num)
        
        for idx in range(len(buckets) - 1, 0, -1):
            for num in buckets[idx]:
                res.append(num)
                if len(res) == k:
                    return res
        