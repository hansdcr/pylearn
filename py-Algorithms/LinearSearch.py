def linear_search(value, arr):
    """ 在list中查找等于5的元素并返回下标 """
    for i in arr:
        if arr[i] == value:
            return i


def linear_search_v2(func, arr):
    """ 改造后，传入一个函数，通过改变传入函数
        的行为，让这个查询函数便的更灵活
    """
    for index, val in enumerate(arr):
        if func(val):
            return index
    return -1


def linear_search_recursion(val, arr):
    """ 用递归的方式实现线性查找 """
    if len(arr) == 0:
        return -1
    index = len(arr) - 1
    if val == arr[index]:
        return index
    return linear_search_recursion(val, arr[0:index])


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    #assert linear_search(5, arr) == 5
    #print(linear_search_v2(lambda x: x == 5, arr))
    #print(linear_search_v2(lambda x: x > 6, arr))
    print(linear_search_recursion(5, arr))