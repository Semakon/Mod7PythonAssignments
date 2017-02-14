from week1.graph import *
import math


class Heap(object):
    """
    Min- or Maxheap objects are binary trees with each node key being smaller or bigger than than its
    children respectively.
    """

    def __init__(self, max=False, E=None):
        """
        Creates a maxheap if `max` is True or a minheap if `max` is False.
        :param E: The list representing the heap.
        :param max: Decides whether the heap will be a minheap or a maxheap.
        """
        self._max = max
        if not E:
            self._data = []
        else:
            self._data = E
            self.build_heap()

    def __repr__(self):
        """
        Programmer friendly representation of the heap object.
        :return: The string representation of the data.
        """
        s = ""
        k = 0
        for i in range(0, len(self._data)):
            s += str(self._data[i])
            if i == 2**k:
                s += "\n"
            k += 1
        return s

    def __str__(self) -> str:
        """
        User friendly representation of the heap object.
        :return: The string representation of the data.
        """
        s = "d=0\t(0)"
        d = 1
        for i in range(0, len(self._data)):
            k = 2**d - 1
            if i == k:
                s += "\nd=" + str(d) + "\t" + "(" + str(d) + ")"
                d += 1
            s += self._str(int(str(self._data[i]))) + "[" + str(d - 1) + "]"

        side, step = 0, 3
        for i in range(d - 1, -1, -1):
            s = s.replace("(" + str(i) + ")", " " * side)
            s = s.replace("[" + str(i) + "]", " " * step)
            side, step = step, step*2 + 3
        return s

    @staticmethod
    def _str(i: int) -> str:
        """
        Takes an integer i, with 0 <= i <= 999, and gives a string representation for the __str__ method.
        :param i: The integer to be represented, 0 <= i <= 999
        :return: A string representation of an integer.
        """
        if i < 0 or i > 999:
            raise ValueError("0 <= i <= 999")
        if 0 <= i <= 9:
            s = "__" + str(i)
        elif 10 <= i <= 99:
            s = "_" + str(i)
        else:
            s = str(i)
        return s

    def build_heap(self, test=False):
        """
        Builds a heap from _data.
        """
        lastparent = (len(self._data) - 2) // 2
        for i in range(lastparent, -1, -1):
            self.heapify(i)

    def heapify(self, i=0):
        """
        Heapifies the the data so it is a proper heap again using either max_heapify or min_heapify.
        :param i: The index of the current node.
        """
        if self._max:
            self._max_heapify(i)
        else:
            self._min_heapify(i)

    def _max_heapify(self, i: int):
        """
        Recursively heapifies the data so it is a maxheap again.
        :param i: The index of the current node.
        """
        left, right = 2*i+1, 2*i+2
        if left < self.heapsize and self._data[left].dist > self._data[i].dist:
            max = left
        else:
            max = i
        if right < self.heapsize and self._data[right].dist > self._data[max].dist:
            max = right  # max is index of max{_data[i], _data[left], _data[right]}
        if max != i:     # so it's not a heap
            self._data[i], self._data[max] = self._data[max], self._data[i]
            self._max_heapify(max)

    def _min_heapify(self, i: int):
        """
        Recursively heapifies the data so it is a minheap again.
        :param i: The index of the current node.
        """
        left, right = 2*i+1, 2*i+2
        if left < self.heapsize and self._data[left].dist < self._data[i].dist:
            min = left
        else:
            min = i
        if right < self.heapsize and self._data[right].dist < self._data[min].dist:
            min = right  # max is index of max{_data[i], _data[left], _data[right]}
        if min != i:     # so it's not a heap
            self._data[i], self._data[min] = self._data[min], self._data[i]
            self._min_heapify(min)

    def insert(self, x: "Vertex"):
        """
        Inserts a new vertex into the heap.
        :param x: The vertex that is to be inserted.
        """
        self._data.append(x)
        self.build_heap()

    def delete(self, x: "Vertex"):
        """
        Deletes a vertex from the heap.
        :param x: The vertex to be deleted.
        """
        self._data.remove(x)
        self.build_heap()

    def in_heap(self, x: "Vertex") -> bool:
        """
        Checks whether a vertex is in the heap.
        :param x: The vertex to be checked
        :return: True if the vertex is in the heap, False if it is not.
        """
        return x in self._data

    def is_not_empty(self) -> bool:
        """
        Checks whether the heap is empty.
        :return: True if the heap is empty, False if it is not.
        """
        return bool(self._data)

    @property
    def top(self) -> "Vertex":
        """
        Returns the top vertex of the heap.
        :return: The top vertex of the heap.
        """
        return self._data[0]

    @property
    def max(self) -> bool:
        """
        Whether this heap is a min- or a maxheap.
        :return: True if maxheap, False if minheap.
        """
        return self._max

    @property
    def heapsize(self) -> int:
        """
        Displays the size of the heap.
        :return: The size of the heap.
        """
        return len(self._data)
