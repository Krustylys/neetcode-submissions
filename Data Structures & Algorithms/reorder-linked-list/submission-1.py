# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        cur = head
        cpy = []
        while cur:
            cpy.append(cur)
            cur = cur.next
        
        i, j = 0, len(cpy) - 1

        while i < j:
            cpy[i].next = cpy[j]
            i+=1
            if i>=j:
                break
            cpy[j].next = cpy[i]
            j-=1
        
        cpy[i].next = None
        
        
    
        
            
