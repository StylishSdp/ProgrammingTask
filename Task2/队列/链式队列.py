class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.__front = ListNode()
        self.__rear = ListNode()

    def push(self, val):
        temp = ListNode(val)
        if self.__rear == None:
            self.__front = temp
        else:
            self.__rear.next = temp

        self.__rear = temp

    def pop(self):
        if self.__front == None:
            return -1
        else:
            temp = self.__front
            self.__front = self.__front.next
            return temp.val

    def peek(self):
        if self.__front == None:
            return -1
        else:
            return self.__front.val

