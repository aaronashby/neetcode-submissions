class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        res = []
        for i in range(len(nums)):
            complements[target - nums[i]] = i
        
        for j in range(len(nums)):
            if complements.get(nums[j], None) != None and complements.get(nums[j], None) != j:
                res.append(j)
                res.append(complements[nums[j]])
                return res
        return res