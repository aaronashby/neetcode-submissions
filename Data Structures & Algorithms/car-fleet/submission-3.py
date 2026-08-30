class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)

        for car in pairs:
            stack.append(car)
            timeToFinish = (target - car[0]) / car[1]

            if len(stack) >= 2 and timeToFinish <= (target - stack[-2][0]) / stack[-2][1]:
                stack.pop()
        
        return len(stack)