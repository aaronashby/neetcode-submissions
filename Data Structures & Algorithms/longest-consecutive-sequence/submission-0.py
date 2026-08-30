class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        streaks = []

        for num in nums_set:
            streak = 1
            curr_num_in_streak = num

            while curr_num_in_streak + 1 in nums_set:
                streak += 1
                curr_num_in_streak += 1
            
            streaks.append(streak)
        
        max_streak = 0
        for num in streaks:
            if num > max_streak:
                max_streak = num
        
        return max_streak
