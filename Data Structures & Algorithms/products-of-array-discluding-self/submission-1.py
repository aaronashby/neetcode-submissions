class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        i = 1

        for num in nums:
            prefix.append(prefix[i - 1] * num)
            i += 1
        
        prefix.append(1)

        for num in reversed(nums):
            suffix.insert(0, suffix[0] * num)
        
        suffix.insert(0, 1)
        res = []
        for i, num in enumerate(nums):
            res.append(prefix[i] * suffix[i + 2])
        
        return res