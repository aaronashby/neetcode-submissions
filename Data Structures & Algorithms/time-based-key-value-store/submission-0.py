class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.time_map[key]) - 1
        res = ("", 0)

        while l <= r:
            mid = (l + r) // 2

            if self.time_map[key][mid][1] > timestamp:
                r = mid - 1
            else:
                if self.time_map[key][mid][1] > res[1]:
                    res = (self.time_map[key][mid][0], self.time_map[key][mid][1])
                l = mid + 1
        return res[0]