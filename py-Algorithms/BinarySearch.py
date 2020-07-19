def binary_search(val, first, last, arr):
    if len(arr) == 0:
        return -1

    if first > last:
        return -1

    mid = (first + last) // 2
    if val < arr[mid]:
        # 在左侧继续查找
        return binary_search(val, first, mid - 1, arr)
    elif val > arr[mid]:
        # 在右侧继续查找
        return binary_search(val, mid + 1, last, arr)
    elif val == arr[mid]:
        return mid


def binary_search_while(val, arr):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if val < arr[mid]:
            last = mid - 1
        elif val > arr[mid]:
            first = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    first = 0
    last = len(arr) - 1
    #print(binary_search(3, first, last, arr))
    print(binary_search_while(5, arr))