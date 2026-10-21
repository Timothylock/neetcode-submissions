class Solution:
    def trap(self, height: List[int]) -> int:
        # Tallest Left  and Talelst Right will tell us at any given position, whats it tallest surrounding point is. Then go through them all
        fromLeft, fromRight = [0] * len(height), [0] * len(height)

        highest = 0
        for i, curHeight in enumerate(height):
            highest = max(highest, curHeight)
            fromLeft[i] = highest

        highest = 0
        for i in range(len(height) - 1, -1, -1):
            curHeight = height[i]
            highest = max(highest, curHeight)
            fromRight[i] = highest

        # Join them all together to get total (through min)
        total = 0
        for i, curHeight in enumerate(height):
            total += min(fromLeft[i], fromRight[i]) - curHeight
        
        return total