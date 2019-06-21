'''

二分查找[递归]
二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。
但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列
'''


# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:

        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1


# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("元素在数组中的索引为 %d" % result)  # --> 元素在数组中的索引为 3
else:
    print("元素不在数组中")
