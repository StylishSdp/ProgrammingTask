class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def isEmpty(self):
        if self.__top == None:
            return True
        else:
            return False

    def getSize(self):
        return self.__size

    def push(self, val):
        node = ListNode(val)
        node.next = self.__top
        self.__top = node

    def pop(self):
        if self.__top == None:
            raise Exception('Stack is null')
        else:
            temp = self.__top
            self.__top = self.__top.next
            return temp.val


stack = Stack()
for i in range(9):
    stack.push(i + 1)

stack.push(11)
stack.pop()


