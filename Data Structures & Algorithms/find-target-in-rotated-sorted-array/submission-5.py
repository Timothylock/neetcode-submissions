class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]

        # Case: Cut is Left: M < R -> So easier to chech right first, then ELSE to left
        # Case: Cut is Right: M > R -> So easier to check left first, then ELSE to right
        if len(nums) == 1 and nums[0] == target:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            valL = nums[l]
            m = (l + r) // 2
            valM = nums[m]
            valR = nums[r]

            if valL == target:
                return l
            elif valM == target:
                return m
            elif valR == target:
                return r

            if valM < valR:
                # Cut is on left. So lets check right and default to left
                if valM < target < valR:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # Cut is on right. So lets check left and default to right
                if valL < target < valM:
                    r = m - 1
                else:
                    l = m + 1
                    
        
        return -1
