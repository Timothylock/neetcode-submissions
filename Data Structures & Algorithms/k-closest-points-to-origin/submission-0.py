class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for pt in points:
            dist = math.sqrt((pt[0])**2 + (pt[1])**2)
            heapq.heappush(hp, (dist, pt))

        res = []
        for i in range(k):
            _, pt = heapq.heappop(hp)
            res.append(pt)

        return res