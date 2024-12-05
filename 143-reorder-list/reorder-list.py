###############################################################################
# Brute force after converting linkedlist to array and trying the logic
    # def reorderList(self, array) -> list:
    #     res = []
    #     p1, p2 = 0, len(array)-1
    #     while p1 <= p2:
    #         res.append(array[p1])
    #         if p1 != p2:
    #             res.append(array[p2])
    #         p1 += 1
    #         p2 -= 1
    #     return res  
############################################################################### 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2