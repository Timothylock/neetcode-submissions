class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            num = nums[i]
            if target - num in dic and dic[target-num] != i:
                return [i, dic[target-num]]
        
        return [0,0]