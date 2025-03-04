# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                start = head  
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start  # Return the node where the cycle begins

        # If no cycle is detected
        return None
        