import math

class Heap:

    def __init__(self, list):
        self.__list = list
        self.__size = len(self.__list)

        self.__build_heap()

    def __build_heap(self):
        n = math.floor(len(self.__list)/2)
        for i in range(0,n+1):
            self.__heapify(n-i)

    def sort(self, key=None, reverse=False):
        list = self.__list
        length = len(list)
        i = self.__size - 1
        while i >= 0:
            list[i], list[0] = list[0], list[i]
            self.__size -= 1
            self.__heapify(0)
            i -= 1
        return self.__list

    def __heapify(self, i):
        list = self.__list
        size = self.__size

        l = Heap.__left(i)
        r = Heap.__right(i)
        largest = i
        if l < size and list[l] > list[largest]:
            largest = l
        if r < size and list[r] > list[largest]:
            largest = r
        if largest != i:
            list[i], list[largest] = list[largest], list[i]
            self.__heapify(largest)

    @staticmethod
    def __parent(i):
        return math.floor(i/2)

    @staticmethod
    def __left(i):
        return 2*i

    @staticmethod
    def __right(i):
        return 2*i+1


v = Heap([1,2,3,5,7,6,8,9,4])

print(v.sort())