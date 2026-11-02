# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers. One at curr, next is n ahead. Once next hits end, we remove curr. 
        prev = None
        curr = head
        forward = head

        # Move forward one by N
        for i in range(0, n):
            forward = forward.next

        # Drive both until forward hits end
        moved = False
        while forward is not None:
            moved = True
            prev = curr
            curr = curr.next
            forward = forward.next

        if not moved:
            return head.next

        # Remove curr Node
        prev.next = curr.next
        return head



    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     tl = self.getLength(head)
    #     goal = tl - n
    #     res = head

    #     if goal == 0:
    #         return head.next

    #     prev = None
    #     for i in range(0, goal):
    #         prev = head
    #         head = head.next

    #     prev.next = head.next
    #     return res

    # def getLength(self, head):
    #     total = 0
    #     while head is not None:
    #         head = head.next
    #         total += 1
    #     return total