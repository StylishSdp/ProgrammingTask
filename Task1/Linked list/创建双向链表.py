class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

class DoubleLinkedList:
    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return self.__head is None

    def length(self):
        current = self.__head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def travel(self):
        current = self.__head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()

    def add(self, val):
        newhead = ListNode(val)
        newhead.next = self.__head
        self.__head = newhead
        newhead.next.pre = newhead

    def append(self, val):
        tail = ListNode(val)
        if self.isEmpty():
            self.__head = tail
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = tail
            tail.pre = current

    def insert(self, index, val):
        node = ListNode(val)
        if index <= 0:
            self.add(val)

        elif index < self.length() - 1:
            self.append(val)

        else:
            current = self.__head
            count  = 0
            while count < index:
                current = current.next
                count += 1
            node.pre = current.pre    #添加node的前驱和后继关系
            current.pre.next = node
            node.next = current
            current.pre = node

    def remove(self, val):
        current = self.__head
        while current:
            if current.val == val:
                if current == self.__head:
                    self.__head = current.next
                    if current.next:
                        current.next.pre = None
                else:
                    current.pre.next = current.next
                    if current.next:
                        current.next.pre = current.pre
                return 'Remove succeed'
            else:
                current = current.next
        return 'Remove failed'

    def search(self, val):
        current = self.__head
        while current:
            if current.val == val:
                return 'Search succeed'
            else:
                current = current.next
        return 'Search failed'


if __name__ == '__main__':
    sll = DoubleLinkedList()

    sll.append(1)
    print(sll.search(1))
    print(sll.remove(1))

    for i in range(5):
        sll.append(i)
    sll.travel()
    sll.add(10)
    sll.travel()
    print(sll.isEmpty())
    print(sll.search(8))
    sll.insert(3,4)
    sll.travel()





