class ListNode(object):
    '''
    节点定义
    '''
    def __init__(self, val):
        self.val = val
        self.next = None

class CircleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node != None:   #头尾相指
            node.next = node

    def isEmpty(self):
        return self.__head is None

    def length(self):
        current = self.__head
        if not current:
            return 0
        current = current.next
        count = 1
        while current != self.__head:
            count += 1
            current = current.next
        return count

    def travel(self):
        '''
        遍历链表
        :return:
        '''
        current = self.__head
        if not current:
            return None
        while current.next != self.__head:
            print(current.val, end=" ")
            current = current.next
        print(current.val)

    #插入删除节点需考虑链表是否为空，是否只有一个头结点，头结点的值等
    def add(self, val):
        '''
        在头部添加节点
        :param val:
        :return:
        '''
        newhead = ListNode(val)
        if self.isEmpty():
            self.__head = newhead
            newhead.next = self.__head
        else:
            current = self.__head
            while current.next != self.__head:
                current = current.next

            newhead.next = self.__head
            self.__head = newhead
            current.next = newhead

    def append(self, val):
        '''
        尾部添加节点
        :param val:
        :return:
        '''
        tail = ListNode(val)
        if self.isEmpty():
            self.__head = tail
            tail.next = self.__head
        else:
            current = self.__head
            while current.next != self.__head:
                current = current.next
            current.next = tail
            tail.next = self.__head


    def insert(self, index, val):
        if index <= 0:
            self.add(val)
        elif index > self.length() - 1:
            self.append(val)
        else:
            node = ListNode(val)
            current = self.__head
            count = 0
            while count < index - 1:
                count += 1
                current = current.next
            node.next = current.next
            current.next = node

    def remove(self, val):
        '''
        删除节点
        :param val:
        :return:
        '''
        current = self.__head
        if current is None:
            return 'Remove failed'
        elif current.val == val:
            if current.next == self.__head:   #是不是只有头结点一个节点
                self.__head = None
                return 'Remove succeed'
            else:
                while current.next != self.__head:
                    current = current.next
                self.__head = current.next
                current.next = self.__head
                return 'Remove succeed'
        else:
            while current.next != self.__head:
                if current.next.val == val:
                    current.next = current.next.next
                    return 'Remove succeed'
                else:
                    current = current.next
            return 'Remove failed'

    def search(self, val):
        '''
        节点是否存在
        :param val:
        :return:
        '''
        current = self.__head
        if current is None:
            return 'Search failed'
        elif current.val == val:
            return 'Search successed'
        else:
            while current.next != self.__head:
                if current.val == val:
                    return 'Search successed'
                else:
                    current = current.next
            if current.val == val:
                return 'Search successed'
            return 'Search failed'


if __name__ == '__main__':
    sll = CircleLinkList()

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
    sll.insert(10,4)
    sll.travel()

