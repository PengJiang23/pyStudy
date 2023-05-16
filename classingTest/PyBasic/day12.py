import random
import time


# 排序算法

class SortTest(object):
    def __init__(self, arr_len=6):
        self.arr = []
        self.arr_len = arr_len
        self.temp_arr = [0] * self.arr_len
        for x in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    # quick sort 交换法
    def partition(self, left, right):
        arr = self.arr
        k = left
        i = left
        while i < right:
            if arr[i] < arr[right]:  # k始终指向要存放比分割值小的下标
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
            i += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick(left, pivot - 1)  # 排左边一半
            self.quick(pivot + 1, right)  # 排右边一半

    # heap
    # ajust heap
    def ajust_maxHeap(self, curr_index, arr_len):
        arr = self.arr
        son = 2 * curr_index + 1
        while son < arr_len:
            if son + 1 < arr_len - 1 and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[curr_index]:
                arr[son], arr[curr_index] = arr[curr_index], arr[son]
                curr_index = son
                son = 2 * curr_index + 1
            else:
                break

    def heap(self):
        arr = self.arr
        # create heap
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.ajust_maxHeap(i, self.arr_len)
        # heap sort
        arr[0], arr[self.arr_len - 1] = arr[self.arr_len - 1], arr[0]
        for i in range(self.arr_len - 1, 1, -1):
            self.ajust_maxHeap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    # merge
    def subsquence_merge(self, low, mid, high):
        temp_arr = self.temp_arr
        arr = self.arr
        temp_arr[low:high + 1] = arr[low:high + 1]
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if temp_arr[i] < temp_arr[j]:
                arr[k] = temp_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = temp_arr[j]
                k += 1
                j += 1
        while i <= mid:
            arr[k] = temp_arr[i]
            k += 1
            i += 1

        while j <= high:
            arr[k] = temp_arr[j]
            k += 1
            j += 1

    def merge(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge(low, mid)
            self.merge(mid + 1, high)
            self.subsquence_merge(low, mid, high)

    # count
    def count_sort(self):
        count_arr = [0] * 100
        i = 0
        arr = self.arr
        while i < len(arr):
            count_arr[arr[i]] += 1
            i += 1
        k = 0
        for i in range(len(count_arr)):
            j = 0
            while j < count_arr[i]:
                arr[k] = i
                k += 1
                j += 1

    # 查找
    # Binary search
    def Binary_search(self, arr, Num: int):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > Num:
                high = mid - 1
            elif arr[mid] < Num:
                low = mid + 1
            else:
                return mid
        return -1

    # hash search
    # test api
    def test(self):
        print(self.arr)
        # self.quick(0, self.arr_len - 1)
        # self.merge(0, self.arr_len -1)
        # self.count_sort()
        print(self.arr)

    def test_time(self):
        start = time.time()
        self.quick(0, self.arr_len - 1)
        end = time.time()
        print(f"{end - start}")


if __name__ == '__main__':
    s1 = SortTest()
    list1 = [0, 5, 8, 10, 22, 45, 50]
    print(s1.Binary_search(list1, 50))
