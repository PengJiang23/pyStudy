#!/user/bin/python3
"""
数据结构学
"""
import random
from collections import deque


# 栈
class StackTest():
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.empty():
            return "empty"
        return self.stack[-1]

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


# 队列
testDeque = deque([1, 2, 3, 4])
testDeque.append(5)


# 循环队列
class Queue():
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0
        self.maxsize = 6

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isfull(self):
        if self.front == (self.rear + 1) % self.maxsize:
            return True
        return False

    def enqueue(self, elem):
        if self.isfull():
            return
        self.queue.append(elem)
        self.rear = (self.rear + 1) % self.maxsize

    def dequeue(self):
        if self.isEmpty():
            return
        self.front = (self.front + 1) % self.maxsize
        return self.queue.pop(0)


# 二叉树
# Node结点
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


# 树
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.queue = []

    # 层次建树
    """
    新增结点，加入队列中
    检查队列第一个结点左右是否为空
    """

    def insert_tree(self, elem):
        new_node = Node(elem)
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)

    def preorder(self, current_node: Node):
        if current_node:
            print(current_node.elem, end='')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def midorder(self, current_node: Node):
        if current_node:
            self.midorder(current_node.lchild)
            print(current_node.elem, end='')
            self.midorder(current_node.rchild)

    def lastorder(self, current_node: Node):
        if current_node:
            self.lastorder(current_node.lchild)
            self.lastorder(current_node.rchild)
            print(current_node.elem, end='')


# 红黑树


"""
算法学习
"""


# 排序
class MySort(object):
    def __init__(self, arr_len=6):
        self.arr = []
        self.arr_len = arr_len

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        """
        冒泡，交换,l-r方向
        :return:
        """
        arr = self.arr
        i = 0
        while i < self.arr_len - 1:
            j = 0
            while j < self.arr_len - 1:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i += 1

    def select(self):
        arr = self.arr
        i = 0
        while i < self.arr_len - 1:
            min_num = i
            j = i + 1
            while j < self.arr_len - 1:
                if arr[j] < arr[min_num]:
                    min_num = j
                j += 1
            arr[i], arr[min_num] = arr[min_num], arr[i]
            i += 1

    # def insert_sort(self):

    def quick(self, low, high):
        """
        快排，递归，找基准，子序列的起始位置
        :return:
        """
        # pivot选取
        arr = self.arr
        if low < high:
            t_index = self.partition(low, high)
            self.quick(low, t_index-1)
            self.quick(t_index+1, high)

    def partition(self, low, high):
        arr = self.arr
        pivot = arr[low]
        while low < high:
            while low < high and pivot <= arr[high]:
                high -= 1
            arr[low] = arr[high]
            while low < high and pivot >= arr[low]:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        return low

    # def shell(self):

    def test_sort(self):
        print(self.arr)
        self.quick(0, self.arr_len - 1)
        print(self.arr)

# 查找


if __name__ == '__main__':
    # stack
    s1 = StackTest()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(5)
    print(s1.empty())
    print(s1.pop())
    print(s1.size())
    print(s1.top())
    # queue test
    print(testDeque)

    # tree test
    b1 = BinaryTree()
    for i in range(1, 5):
        b1.insert_tree(i)
    b1.preorder(b1.root)
    print()
    b1.midorder(b1.root)
    print()

    # sort
    sort1 = MySort()
    sort1.random_int()
    sort1.test_sort()
