class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        #如果使用k个空间存储k个值，当front == rear时，无法判断队列是空还是满
        #所以牺牲一个空间，使用k+1个空间存储k个数
        self.__length = k + 1
        self.__data = [None] * self.__length
        self.__front = 0   #队头队尾索引都是0
        self.__rear = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            #队尾元素入队时，先赋值，后设置rear = (rear+1) % length
            self.__data[self.__rear] = value
            self.__rear = (self.__rear + 1) % self.__length
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            #队头元素出队时，front = (front + 1) % length
            self.__front = (self.__front + 1) % self.__length
            return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__data[self.__front]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__data[(self.__rear - 1 + self.__length) % self.__length]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        #front == rear时，为空
        if self.__front == self.__rear:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        # (rear + 1)%length == front
        if (self.__rear + 1) % self.__length == self.__front:
            return True
        else:
            return False