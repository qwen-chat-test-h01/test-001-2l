def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    # 创建数组的副本，避免修改原数组
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮结束后最大元素会"冒泡"到末尾，所以范围逐渐缩小
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return sorted_arr


def bubble_sort_inplace(arr):
    """
    原地冒泡排序（直接修改原数组）
    
    参数:
        arr: 待排序的列表
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


# 示例用法和测试
if __name__ == "__main__":
    # 测试数据
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    # 使用非原地排序
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array)
    
    # 使用原地排序
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    print("\n原始数组:", test_array2)
    bubble_sort_inplace(test_array2)
    print("原地排序后:", test_array2)
    
    # 额外测试用例
    print("\n其他测试用例:")
    print("空数组:", bubble_sort([]))
    print("单个元素:", bubble_sort([1]))
    print("已排序数组:", bubble_sort([1, 2, 3, 4, 5]))
    print("逆序数组:", bubble_sort([5, 4, 3, 2, 1]))
    print("有重复元素:", bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]))