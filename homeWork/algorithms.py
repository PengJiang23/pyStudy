# 每日一练
# quick sort
def quick(arr: list, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick(arr, low, partition_index - 1)
        quick(arr, partition_index + 1, high)


def partition(arr: list, low, high):
    i = low  # 工作指针
    k = low  # 分割指针
    while i < high:  # 交换法,以high为枢轴元素
        if arr[i] < arr[high]:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        i += 1
    arr[k], arr[high] = arr[high], arr[k]
    return k


# heap
def ajust_max(arr: list, cur_index, arr_len):
    child = 2 * cur_index + 1
    while child < arr_len:
        if child + 1 < arr_len - 1 and arr[child] < arr[child + 1]:
            child += 1
        if arr[cur_index] < arr[child]:
            arr[cur_index], arr[child] = arr[child], arr[cur_index]
            cur_index = child  # 调整子节点
            child = 2 * cur_index + 1
        else:
            break


def heap(arr: list):
    # 建立大根堆
    for i in range(len(arr) // 2, -1, -1):
        ajust_max(arr, i, len(arr))
    # 堆排序
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
    for i in range(len(arr) - 1, -1, -1):
        ajust_max(0, i)
        arr[0], arr[i - 1] = arr[i - 1], arr[0]


# merge
# count
# 层次建树
# RBT

if __name__ == '__main__':
    arr = [5, 8, 10, 4, 12, 7]
    print(arr)
    quick(arr, 0, len(arr) - 1)
    print(arr)
