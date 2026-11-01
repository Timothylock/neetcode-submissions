# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        ptr1 = head
        if head.next is None:
            return False
        ptr2 = head.next

        while ptr1 != ptr2:
            if ptr2.next is None:
                return False
            if ptr2.next.next is None:
                return False

            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
        
        return True