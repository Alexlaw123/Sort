def insertion_sort(arr):
  """插入排序算法

  Args:
    arr: 待排序的数组

  Returns:
    排序后的数组
  """

  for i in range(1, len(arr)):
    key = arr[i]  # 当前要插入的元素
    j = i - 1

    # 将大于key的元素向后移动一位
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    # 将key插入到正确的位置
    arr[j + 1] = key

  return arr

# 示例用法
if __name__ == "__main__":
  unsorted_list = [64, 34, 25, 12, 22, 11, 90]
  print("未排序的数组:", unsorted_list)

  sorted_list = insertion_sort(unsorted_list)
  print("排序后的数组:", sorted_list)