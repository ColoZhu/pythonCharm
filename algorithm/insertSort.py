'''
插入排序


'''


def insertionSort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]

        j = i - 1  # 内部循环从i-1(当前元素前一位)位置开始往前依次比较大小
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  # 大数往后挪
            j -= 1
        arr[j + 1] = temp  # 小数往前挪


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("排序后的数组:", arr)
