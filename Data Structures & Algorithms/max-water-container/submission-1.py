class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curr_max = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            curr_max = max(area, curr_max)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return curr_max