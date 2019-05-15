class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head     #快慢指针，如果有环，fast和slow会相遇
        slow = head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True

        return False
