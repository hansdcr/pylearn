def numOfSubarrays(arr, k ,threshold):
    """
    给你一个整数数组 arr 和两个整数 k 和 threshold 。

    请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
    输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    输出：3
    解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
    """

    total = 0 # 满足条件的数组个数
    addSum = 0 # k个数相加的和. 比如: 2+2+2
    target = k * threshold # 平均数 k * threshold

    if len(arr) < k:
        return 0

    addSum = sum(arr[:k])
    if addSum >= target:
        total += 1
    for i in range(k, len(arr)): # 主要理解这个循环，怎么达到滑动窗口效果的
        addSum = addSum + arr[i] - arr[i-k]
        if addSum >= target:
            total += 1

    print(total)
    return total


if __name__ == "__main__":
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    numOfSubarrays(arr, k, threshold)

