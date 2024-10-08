def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""
    result = []
    i = j = 0
    #count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            #count = count + len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
A = [12, 3, 7, 9, 14, 6, 11, 2]
sorted_A = merge_sort(A)
print(sorted_A)
