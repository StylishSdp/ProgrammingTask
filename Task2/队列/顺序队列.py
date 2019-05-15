class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__data = []
        self.__front = -1
        self.__rear = -1

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.__data.append(x)
        self.__rear += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.__rear == -1:
            return -1
        else:
            self.__rear -= 1
            return self.__data.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.__rear == -1:
            return -1
        else:
            return self.__data[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.__rear == -1:
            return True
        else:
            return False
