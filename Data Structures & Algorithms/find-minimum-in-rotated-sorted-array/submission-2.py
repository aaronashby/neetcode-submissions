class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1000
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[l] < nums[r] or nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res