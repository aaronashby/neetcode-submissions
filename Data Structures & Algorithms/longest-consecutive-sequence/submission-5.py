class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums to a hash set
        # For each num in nums
        # - If it's the beginning of a sequence (num - 1 isn't in the set), count sequence
        #   and track max
        # - If not, then skip
        numsSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numsSet:
                curr, length = num + 1, 1
                while curr in numsSet:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest