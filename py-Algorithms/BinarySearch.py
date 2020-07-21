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


def findMin(nums):
    """
    假设按照升序排序的数组在预先未知的某个点上进行了旋转
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素

    思路一： 数组的第一个元素和最后一个元素对比
            如果第一个元素大于最后一个元素，继续比较第二个元素和最后一个元素大小，一次类推
            如果当前元素不在比最后一个元素大，那么当前元素就是最小值
    """
    if len(nums) == 0:
        return - 1
    for idx, val in enumerate(nums):
        if val > nums[-1]:
            pass
        else:
            return val, idx


def findMin_v2(nums):
    """ findMin的递归实现"""
    if len(nums) == 0:
        return - 1

    if nums[0] > nums[-1]:
        return findMin_v2(nums[1:])
    else:
        return nums[0]


def searchRange(nums, target, first, last):
    """
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:

    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]

    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
    """
    if len(nums) == 0:
        return -1
    mid = (first + last) // 2
    if target < nums[mid]:
        return searchRange(nums, target, first, mid - 1)
    elif target > nums[mid]:
        first = mid + 1
        return searchRange(nums, target, mid + 1, last)
    else:
        # 由于有重复数字，这个值可能在左测，也可能在右测
        idx_list = []
        # 向左看
        # 向右看
        pass


if __name__ == "__main__":
    #arr = [0, 1, 2, 3, 4, 5, 6, 7]
    #arr = [0, 1, 2, 3, 5, 6, 7]
    #first = 0
    #last = len(arr) - 1
    #print(binary_search(3, first, last, arr))
    #print(binary_search_while(5, arr))
    #print(binary_search_bisect(4, first, last, arr))

    #nums = [4, 5, 6, 7, 0, 1, 2]
    #print(findMin(nums))
    #print(findMin_v2(nums))

    nums = [5, 7, 7, 8, 8, 10]
    first = 0
    last = len(nums) - 1
    print(searchRange(nums, 8, first, last))


