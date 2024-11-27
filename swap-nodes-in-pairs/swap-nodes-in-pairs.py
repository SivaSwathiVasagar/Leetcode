# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev , cur = dummy, head
        while cur and cur.next:
            # backing up the 3rd node and second
            nextPair = cur.next.next
            second = cur.next
            
            # Updating next values
            second.next = cur
            cur.next = nextPair
            prev.next = second
            
            # Changing current and previous values
            prev = cur
            cur = nextPair
        return dummy.next
            
            
           
  
        
                
        