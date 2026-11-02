"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Copy list first, keeping dict of what the map is
        oldToNew = {}
        curr = head
        newCurr = res = Node(head.val)
        while curr is not None:
            newCurr.val = curr.val
            temp = Node(0)
            if curr.next is None:
                newCurr.next = None
            else:
                newCurr.next = temp

            oldToNew[curr] = newCurr
            newCurr = newCurr.next
            curr = curr.next

        # Link the RANDOMs correctly based on the dict
        curr = head
        newRes = res
        while curr is not None:
            if curr.random is not None:
                newRes.random = oldToNew[curr.random]
            curr = curr.next
            newRes = newRes.next

        return res


        # Edge CAse? None at the end? 
        