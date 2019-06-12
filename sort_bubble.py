# 冒泡排序


def bubbleSort(list):
    for i in range(len(list) - 1):  # 只用遍历n-1次,list最后一个数在内部循环里面比较大小
        flag = False  # 设置是否有元素交换的标志，false表示没有，true表示有元素进行交换
        for j in range(len(list) - i - 1):  # ｊ为列表下标,比较找出i后面一组数最小的
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # 小数左边放,大数右边放
                flag = True  # 交换位置后设置为True

        if (not flag):
            break;  # 没有交换过,说明后面的顺序是OK的,直接中断外层循环

    return list


# 调用排序
listSrc = [1, 2, 5, 4, 0, 3, 6]
listSrc1 = [5, 8, 4, 1, 2, 9]
print(bubbleSort(listSrc))
print(bubbleSort(listSrc1))

# 算法改进:在某些情况下，可能在第i趟时元素就已经全部排好序了，此时我们就不必在再进行后面几趟的比较了。
