def merge_sort(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid+1:])

    return merge_sorted_list(left, right)


def merge_sorted_list(left, right):
    length_a, length_b = len(left), len(right)
    a = b = 0
    new_list = []
    while a < length_a and b < length_b:
        if left[a] < right[b]:
            new_list.append(a)
            a +=1
        else:
            new_list.append(b)
            b +=1
    if a < length_a:
        new_list.extend(length_a[a:])
    else:
        new_list.extend(length_b[b:])
    return new_list
