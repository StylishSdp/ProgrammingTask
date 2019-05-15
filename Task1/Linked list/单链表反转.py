class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        pre = None
        current = head
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre