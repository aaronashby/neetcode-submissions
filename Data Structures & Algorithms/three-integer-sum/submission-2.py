class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, i = [], 0

        while i < len(nums) - 1:
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) * -1 in nums[j + 1:]:
                    triple = []
                    triple.append(nums[i])
                    triple.append(nums[j])
                    triple.append((nums[i] + nums[j]) * -1)

                    if triple not in res:
                        res.append(triple)
            i += 1
        return res
            