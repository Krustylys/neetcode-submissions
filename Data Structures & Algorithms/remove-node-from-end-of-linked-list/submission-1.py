# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #iteration

        nodes = 0
        cur = head 
        while cur:
            nodes += 1
            cur = cur.next
        
        rmv_node = nodes - n


        if rmv_node == 0:
            return head.next
        cur = head
        c = 0

        while cur:
            c += 1
            if c == rmv_node:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head
