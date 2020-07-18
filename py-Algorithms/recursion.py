def countdown(i):
    if i >= 1:
        print(i)
        countdown(i-1)


def factorial(x):
    if x == 1:
        return  1
    else:
        return x * factorial(x-1)


def sum(arr):
    print(arr)
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])


def sum2(arr):
    sum = 0
    for i in arr:
        sum +=i
    print(sum)

def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

def max(arr):
    m = 0
    if len(arr) == 1:
        return arr[0]
    if arr[0] > max(arr[1:]):
        m = arr[0]
    else:
        m = max(arr[1:])
    return m



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    #countdown(3)
    # sum([1,2,3,4])
    #sum2([1,2,3,4])
    #print(count(arr))
    print(max(arr))
    pass