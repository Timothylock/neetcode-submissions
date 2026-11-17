class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        val = 0
        for _ in range(k):
            val = heapq.heappop_max(nums)

        return val