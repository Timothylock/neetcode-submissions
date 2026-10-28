class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        l, r = 0, len(nums) - 1
        res = math.inf

        while l < r:
            middle = (l+r)//2
            atLeft = nums[l]
            atMiddle = nums[middle]
            atRight = nums[r]
            # print(atLeft, atMiddle, atRight)
            res = min(res, atMiddle, atLeft, atRight)

            # Case 1 - l < m < r -> on left    | 1, 2, 3, 4, 5, 6
            # Case 2 - l < m > r -> on right   | 4, 5, 6, 1, 2, 3
            # Case 3 - l > m < r -> on left    | 6, 1, 2, 3, 4, 5
            # Case 4 - l > m > r ... shouldnt happen ?

            # Left - m < r
            # right - m > r

            if atMiddle < atRight:
                r = middle - 1
            else:
                l = middle + 1

            # print(l, r)

        return res

            
        