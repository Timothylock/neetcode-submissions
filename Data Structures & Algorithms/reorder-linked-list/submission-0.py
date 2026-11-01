# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.getLength(head)
        mid = math.ceil(length / 2)

        # Get Mid+1 Node and set mid node.next = None
        midNode = head
        for i in range(mid - 1):
            midNode = midNode.next
        list2 = midNode.next
        midNode.next = None

        list2 = self.reverseList(list2)
        
        # Insert
        curr = head
        while list2 is not None:
            temp = curr.next
            temp2 = list2.next
            curr.next = list2
            curr.next.next = temp
            list2 = temp2
            curr = temp

        print(midNode.val)
        print(length, mid)


    def getLength(self, head) -> int:
        total = 0
        while head != None:
            head = head.next
            total += 1

        return total

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        cur = head
        temp = head.next

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev