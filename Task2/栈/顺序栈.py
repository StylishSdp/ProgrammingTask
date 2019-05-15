class Stack:
    def __init__(self, length = 10):
        self.__length = length
        self.__size = 0
        self.__data = [None] * self.__length
        self.__top = -1

    def isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def push(self, val):
        if self.__top >= self.__length - 1:
            raise Exception('Stack is full')
        else:
            self.__top += 1
            self.__data[self.__top] = val
            self.__size += 1

    def pop(self):
        if self.__top == -1:
            raise Exception('Stack is null')

        else:
            val = self.__data[self.__top]
            del self.__data[self.__top]
            self.__top -= 1
            self.__size -= 1
            return val


stack = Stack()
for i in range(9):
    stack.push(i + 1)

stack.push(11)
stack.pop()
