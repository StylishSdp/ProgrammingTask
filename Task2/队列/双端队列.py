class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.__data = []
        self.__length = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.__data.insert(0, value)
            return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.__data.append(value)
            return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.__data.pop(0)
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.__data.pop()
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__data[0]

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__data[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.__data) == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.__data) == self.__length:
            return True
        else:
            return False