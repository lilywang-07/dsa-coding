class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])
        return

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        l = 0
        r = len(values)-1
        time = 0
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                time = mid
                l = mid + 1
        if values and values[time][0] <= timestamp:
            return values[time][1]
        return ""
