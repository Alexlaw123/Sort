def partition(arr, low, high):
    # 选择最后一个元素作为基准
    pivot = arr[high]

    # i 是较小元素的索引
    i = low - 1

    # 遍历数组，进行分区
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # 交换 arr[i] 和 arr[j] 的位置
            arr[i], arr[j] = arr[j], arr[i]

    # 最后，将基准元素放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # 返回基准元素的正确位置
    return i + 1


def quick_sort_in_place(arr, low, high):
    if low < high:
        # 找到基准位置，进行分区
        pi = partition(arr, low, high)

        # 递归地对基准位置的左边和右边子数组排序
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)


# 测试快速排序
arr = [33, 10, 59, 26, 41, 85, 19, 2]
quick_sort_in_place(arr, 0, len(arr) - 1)
print("排序后的数组:", arr)
