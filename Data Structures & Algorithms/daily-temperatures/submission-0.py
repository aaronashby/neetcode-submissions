class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        count = 0

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    break
                elif j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    count = 0
            res.append(count)
            count = 0

        return res