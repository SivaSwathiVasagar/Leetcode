# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
        prev = None
        current = head
        while current:
            dummy = current.next
            current.next = prev
            prev = current
            current = dummy
        return prev
            
        