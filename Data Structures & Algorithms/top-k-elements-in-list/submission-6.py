class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        for num, freq in frequencies.items():
            buckets[freq].append(num)
        
        print(buckets)
        for bucket in reversed(buckets):
            if len(res) == k:
                return res
            res += bucket