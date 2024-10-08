def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_extract_max(arr):
    n = len(arr)
    if n == 0:
        return None

    max_value = arr[0]
    arr[0] = arr[n-1]
    arr.pop()
    max_heapify(arr, len(arr), 0)
    return max_value

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# 测试
arr = [12, 11, 13, 5, 6, 7]
print("原数组:", arr)

build_max_heap(arr)
print("构建最大堆:", arr)

max_value = heap_extract_max(arr)
print("删除堆顶元素后的数组:", arr)
print("堆顶最大值:", max_value)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("堆排序结果:", arr)
