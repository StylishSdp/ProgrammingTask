# #实现动态扩容的数组
#
class Array:
    '''
    数组初始化
    length 数组占用内存大小
    size  数组中元素个数
    '''
    def __init__(self, length = 10):
        self.__length = length
        self.__size = 0
        self.__data = [None] * length

    def __getitem__(self, item):
        return self.__data[item]

    def __resize(self, length):
        '''
        数组占用空间扩容或缩容
        :param length:
        :return:
        '''
        new_array = Array(length)
        for i in range(self.__size):
            new_array.__data[i] = self.__data[i]
        self.__data = new_array.__data
        self.__length = new_array.getLength()

    def isEmpty(self):
        return True if self.__size == 0 else False

    def getSize(self):
        return self.__size

    def getLength(self):
        return self.__length

    def getVal(self, index):
        '''
        根据index，查找元素
        :param index:
        :return:
        '''
        if index < 0 or index >= self.__size:
            raise Exception('Index is out of the range.')
        return self.__getitem__(index)

    def valIsIN(self, val):
        '''
        val是否在数组中
        :param val:
        :return:
        '''
        for i in range(self.__length):
            if self.__data[i] == val:
                return True
        return False

    def getIndex(self, val):
        '''
        获取val的index
        :param val:
        :return:
        '''
        for i in range(self.__length):
            if self.__data[i] == val:
                return i
        raise Exception('Value is not in Array.')

    def valModify(self, index, val):
        '''
        根据index修改数组val
        :param index:
        :param val:
        :return:
        '''
        if index < 0 or index >= self.__length:
            raise Exception('Index is out of the range.')

        self.__data[index] = val

    def addVal(self, index, val):
        '''
        添加数组元素
        :param index:
        :param val:
        :return:
        '''
        if index < 0 or index > self.__size:
            raise Exception('Index is invalid.')

        if self.__length - 1== self.__size:
            self.__resize(2 * self.__length)
        for i in range(self.__size, index-1, -1):
            self.__data[i+1] = self.__data[i]

        self.__data[index] = val
        self.__size += 1

    def removeVal(self, index):
        '''
        删除数组元素
        :param index:
        :return:
        '''
        if index < 0 or index >= self.__size:
            raise Exception('Index is out of the range.')
        res = self.__data[index]

        for i in range(index, self.__size):
            self.__data[i] = self.__data[i+1]

        self.__data[self.__size-1] = None
        self.__size -= 1

        if self.__size and self.__length // self.__size >= 4:
            self.__resize(self.__length // 2)
        return res

    def printArray(self):
        print('[', end = '')
        for i in range(self.__length):
            print(self.__data[i], end=' ' if i < self.__length-1 else '')
        print(']')


#测试
test = Array()
for i in range(10):
    test.addVal(i, i+1)
print(test.getSize())
print(test.getLength())
print(test.isEmpty())

test.addVal(8,-1)
test.printArray()
print(test.getVal(3))
test.valModify(2, -2)
test.printArray()
print(test.valIsIN(10))
print(test.getIndex(4))
test.removeVal(3)
test.printArray()
for i in range(19):
    test.addVal(i, i)
test.printArray()
for i in range(1,19):
    test.removeVal(0)
test.printArray()
