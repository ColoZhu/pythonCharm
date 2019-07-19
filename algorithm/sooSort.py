'''
Python 快速排序
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
步骤为：
挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;

分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
'''


# 子序列排序
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引,最开始-1
    pivot = arr[high]  # 基准值

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1  # 从0开始
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素位置
            print(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 交换元素位置
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(arr)

        quickSort(arr, low, pi - 1)  # 排序
        print(arr)
        quickSort(arr, pi + 1, high)
        print(arr)


#测试demo
arr = [10, 7, 3, 8, 2, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:", arr)  # -->排序后的数组: [1, 5, 7, 8, 9, 10]
