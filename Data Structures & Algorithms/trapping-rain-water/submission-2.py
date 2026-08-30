class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(leftMax - height[l], 0)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(rightMax - height[r], 0)
        
        return res