class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSeen = 101
        ret = 0

        for price in prices:
            minSeen = min(minSeen, price)
            ret = max(ret, price - minSeen)

        return ret