def bubble_sort(arr):
    """
    冒泡排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生了交换，用于优化
        swapped = False
        
        # 最后i个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素比下一个元素大，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    print(f"初始数组: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i + 1} 轮排序:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"  交换 {arr[j]} 和 {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  当前数组: {arr}")
        
        if not swapped:
            print("  没有发生交换，排序完成")
            break
        else:
            print(f"第 {i + 1} 轮结束: {arr}")
    
    return arr


# 示例用法
if __name__ == "__main__":
    # 测试基本冒泡排序
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("排序后数组:", sorted_array)
    
    print("\n" + "="*50)
    
    # 测试带步骤显示的冒泡排序
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_with_steps(test_array2)
    
    print("\n" + "="*50)
    
    # 测试已经排序的数组（验证优化效果）
    sorted_test = [1, 2, 3, 4, 5]
    print(f"\n已排序数组测试: {sorted_test}")
    result = bubble_sort(sorted_test)
    print(f"结果: {result}")