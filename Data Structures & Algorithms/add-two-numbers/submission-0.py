# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curL1 = l1
        curL2 = l2
        prev = None
        carryOver = 0

        while curL1 is not None or curL2 is not None:
            print(curL1, curL2)
            if curL2 is not None and curL1 is not None:
                curL1.val += curL2.val
            if curL1 is None:
                curL1 = ListNode(curL2.val)
                prev.next = curL1

            # Handle Carry Over
            curL1.val += carryOver
            carryOver = 0
            if curL1.val >= 10:
                curL1.val -= 10
                carryOver += 1

            prev = curL1
            curL1 = curL1.next
            if curL2 is not None:
                curL2 = curL2.next

        # Need to add one final node
        if carryOver == 1:
            prev.next = ListNode(1)

        return l1