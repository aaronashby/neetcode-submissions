class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                threeSum = num + nums[j] + nums[k]

                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res