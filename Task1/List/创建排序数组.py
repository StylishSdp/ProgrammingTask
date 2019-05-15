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

    def isEmpty(self):
        return True if self.__size == 0 else False

    def getSize(self):
        return self.__size

    def getLength(self):
        return self.__length

    def sorted(self):
        if self.__size <= 1:
            return self.__data
        for i in range(1, self.__size):
            j = i
            target = self.__data[i]  # 每次循环的一个待插入的数
            while j > 0 and target < self.__data[j - 1]:  # 比较、后移，给target腾位置
                self.__data[j] = self.__data[j - 1]
                j = j - 1
            self.__data[j] = target  # 把target插到空位
        return self.__data

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
        if index < 0 or index > self.__size:
            raise Exception('Index is invalid.')

        self.__data[index] = val
        self.sorted()

    def addVal(self, index, val):
        '''
        添加数组元素
        :param index:
        :param val:
        :return:
        '''
        if index < 0 or index > self.__size:
            raise Exception('Index is invalid.')
        #
        if self.__length - self.__size != 1:
            for i in range(self.__size, index-1, -1):
                self.__data[i + 1] = self.__data[i]

        else:
            self.__data[index + 1:] = self.__data[index:-1]
            self.__data[index] = val

        self.__data[index] = val
        self.__size += 1
        self.sorted()

    def removeVal(self, index):
        '''
        删除数组元素
        :param index:
        :return:
        '''
        if index < 0 or index >= self.__size:
            raise Exception('Index is out of the range.')
        res = self.__data[index]

        for i in range(index + 1, self.__length):
            self.__data[i -1 ] = self.__data[i]

        self.__data[self.__size-1] = None
        self.__size -= 1

        self.sorted()

    def printArray(self):
        print('[', end = '')
        for i in range(self.__length):
            print(self.__data[i], end=' ' if i < self.__length-1 else '')
        print(']')


#测试
test = Array()
for i in range(9):
    test.addVal(i, (i+1) % 4)
print(test.getSize())
print(test.getLength())
print(test.isEmpty())
test.printArray()
test.valModify(3,6)
test.printArray()
test.addVal(2,10)
test.printArray()
test.removeVal(6)
test.printArray()


