# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Travel along list 1, merging list 2

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list2.val < list1.val:
            temp1 = list1
            list1 = list2
            list2 = temp1
            

        curList1, curList2 = list1, list2
        while curList1.next is not None:
            list1Next = curList1.next
            if curList2 is not None and curList2.val <= list1Next.val:
                temp = curList2.next
                curList1.next = curList2
                curList1.next.next = list1Next

                curList2 = temp
            curList1 = curList1.next

        curList1.next = curList2
        
        return list1
