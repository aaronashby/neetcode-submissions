class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque() # indices
        l = r = 0

        while r < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)

            # remove left val from window
            if l > queue[0]:
                queue.popleft()
            
            # ensure our window is size k
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        return res