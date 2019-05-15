class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head) :
        '''
        快慢指针，fast一个走两个，slow一次走一个，fast走到末尾，slow走到中间
        :param head:
        :return:
        '''
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow