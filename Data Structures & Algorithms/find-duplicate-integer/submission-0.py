class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyds circular algo. One slow, one fast, we go to the index outlined by the val. 
        # The index will never exceed the len of the array
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow