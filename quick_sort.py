def partition(arr, start, end):

    pivot_index = (end + start) // 2

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    item_from_left_index = start
    item_from_right_index = end

    while True:

        while (arr[item_from_left_index] >= arr[end]) and (item_from_left_index < end):
            item_from_left_index += 1

        while (arr[item_from_right_index] <= arr[end]) and (item_from_right_index > start):
            item_from_right_index -= 1

        if item_from_left_index < item_from_right_index:
            arr[item_from_left_index], arr[item_from_right_index] = arr[item_from_right_index], arr[item_from_left_index]
        else:
            break

    arr[end], arr[item_from_left_index] = arr[item_from_left_index], arr[end]
    return item_from_left_index


def quick_sort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quick_sort(arr, start, p-1)
    quick_sort(arr, p+1, end)