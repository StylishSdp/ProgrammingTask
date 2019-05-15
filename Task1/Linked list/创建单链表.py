class ListNode(object):
    '''
    节点定义
    '''
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return self.__head is None

    def length(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def travel(self):
        '''
        遍历链表
        :return:
        '''
        current = self.__head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def add(self, val):
        '''
        在头部添加节点
        :param val:
        :return:
        '''
        newhead = ListNode(val)
        newhead.next = self.__head
        self.__head = newhead

    def append(self, val):
        '''
        尾部添加节点
        :param val:
        :return:
        '''
        tail = ListNode(val)
        if self.isEmpty():
            self.__head = tail
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = tail


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

        if self.__head is None:  # 判断是不是空链表
            return 'LinkedList is NULL'

        elif current.val == val:  # 判断是不是头结点
            self.__head = current.next
            return 'Remove successed'
        else:
            while current.next:
                if current.next.val == val:
                    current.next = current.next.next
                    return 'Remove successed'
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
        while current != None:
            if current.val == val:
                return 'Search successed'
            else:
                current = current.next
        return 'Search failed'


if __name__ == '__main__':
    sll = SingleLinkList()

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

