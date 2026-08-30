class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, a in enumerate(nums):
            l, r = idx + 1, len(nums) - 1

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            while l < r:
                b, c = nums[l], nums[r]

                if a + b + c > 0:
                    r -= 1
                elif a + b + c < 0:
                    l += 1
                else:
                    res.append([a, b, c])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res