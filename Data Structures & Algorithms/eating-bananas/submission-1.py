class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        ans = upper

        while lower <= upper:
            middle = (upper + lower) // 2

            req = self.hoursRequired(piles, middle)
            if req <= h:
                ans = middle
                upper = middle - 1
            else:
                lower = middle + 1
        
        return ans

    def hoursRequired(self, piles, rate) -> int:
        hours = 0
        for slot in piles:
            hours += math.ceil(slot / rate)
        
        return hours