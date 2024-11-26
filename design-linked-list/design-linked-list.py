class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        current = self.left.next
        while current != self.right and index > 0:
            current = current.next
            index -=1
        if current and current != self.right and index == 0:    
            return current.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        next = self.left.next
        prev = self.left
# Neetcode easy assinging 
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        # node.prev = self.left
        # node.next = self.left.next
        # self.left.next.prev = node
        # self.left.next = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node 

    def addAtIndex(self, index: int, val: int) -> None:
        if self.left.next is None or index < 0:
            return -1
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and index == 0:
            node = ListNode(val)
            next = current
            prev = current.prev

            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        if self.left.next is None and index < 0:
            return -1
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.right and index == 0:
            next = current.next
            prev = current.prev

            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)