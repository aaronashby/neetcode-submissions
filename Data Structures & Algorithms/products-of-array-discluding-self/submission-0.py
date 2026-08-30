class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx - 1] * nums[idx - 1]
        
        for idx in range(len(nums) - 2, -1, -1):
            suffix[idx] = suffix[idx + 1] * nums[idx + 1]
        
        res = [1] * len(nums)
        for idx in range(len(nums)):
            res[idx] = prefix[idx] * suffix[idx]
        
        return res

