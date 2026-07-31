# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head 
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        rmv_idx = len(nodes) - n

        if rmv_idx == 0:
            return head.next

        nodes[rmv_idx - 1].next = nodes[rmv_idx].next 
        return head
        

