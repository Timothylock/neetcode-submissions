class TimeMap:

    def __init__(self):
        self.timestamps = {}
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = [timestamp]
        else:
            self.timestamps[key].append(timestamp)

        if key not in self.data:
            self.data[key] = [value]
        else:
            self.data[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""

        validTimestamps = self.timestamps[key]
        data = self.data[key]

        if validTimestamps[0] > timestamp:
            return ""

        # BST
        lastValidIndex = 0
        l, r = 0, len(validTimestamps) - 1
        while l <= r:
            m = (l + r) // 2
            valL = validTimestamps[l]
            valM = validTimestamps[m]
            valR = validTimestamps[r]

            if valL <= timestamp:
                lastValidIndex = l
                if valL == timestamp:
                    break

            if valM <= timestamp:
                lastValidIndex = m
                if valM == timestamp:
                    break
                l = m + 1
            elif valM > timestamp:
                r = m - 1
            

        return data[lastValidIndex]

        
        
