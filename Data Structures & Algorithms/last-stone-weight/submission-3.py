class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            cur = abs(heapq.heappop_max(stones) - heapq.heappop_max(stones))
            heapq.heappush_max(stones, cur)
        return heapq.heappop_max(stones)