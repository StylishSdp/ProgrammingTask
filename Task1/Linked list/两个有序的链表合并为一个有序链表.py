#leetcode 21

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        head = ListNode(0)   #链表类题目：1.先生成一个头结点  2.单指针节点或双指针节点
        temp = head         #关键点：指针的移动
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return head.next
