class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []
        l = r = 0
        if len(nums) == 1:
            return [nums[0]]
        
        while r < len(nums):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if r >= (k - 1):
                output.append(queue[0])
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1
            r += 1
        return output
                