class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            height = heights[i]
            width = 1
            maxArea = max(maxArea, heights[i])

            for j in range(i + 1, len(heights)):
                height = min(height, heights[j])
                width += 1
                maxArea = max(maxArea, height * width)
        
        return maxArea