class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] + nums[j] == -nums[k]

        # EC: -1, -1, 2  |      -1 + -1 == -2
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                ts = val + nums[l] + nums[r]
                # Handles two same fine as it will just loop twice
                if ts > 0:
                    r -= 1
                elif ts < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])

                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

        return res

