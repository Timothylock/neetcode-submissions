class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.t = nums
        self.k = k

    def add(self, val: int) -> int:
        self.t.append(val)
        self.t.sort()
        return self.t[len(self.t) - self.k]

