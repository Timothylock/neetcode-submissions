class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromLeft = [nums[0]] * len(nums)
        fromRight = [nums[len(nums) - 1]] * len(nums)

        soFar = nums[0]
        for i in range(1, len(nums)):
            soFar = soFar * nums[i]
            fromLeft[i] = soFar

        soFar = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            soFar = soFar * nums[i]
            fromRight[i] = soFar

        final = [fromRight[1]] * len(nums)
        final[len(nums) - 1] = fromLeft[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            final[i] = fromLeft[i-1] * fromRight[i+1]
            
        return final
            

