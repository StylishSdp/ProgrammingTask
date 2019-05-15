class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):   #由leetcode21题合并两个有序链表，借此合并K个有序链表
        ans = ListNode(0)
        res = ans
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next

        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return ans.next

    def mergeKLists(self, lists):
        if lists == []:
            return []
        L = len(lists)
        res = lists[0]
        for i in range(1, L):
            res = self.mergeTwoLists(res, lists[i])

        return res
