# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tl = self.getLength(head)
        goal = tl - n
        res = head

        if goal == 0:
            return head.next

        prev = None
        for i in range(0, goal):
            prev = head
            head = head.next

        prev.next = head.next
        return res

    def getLength(self, head):
        total = 0
        while head is not None:
            head = head.next
            total += 1
        return total