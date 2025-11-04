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
        
        # 如果没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    print(f"初始数组: {arr}")
    n = len(arr)
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i + 1} 轮排序:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"  交换 {arr[j]} 和 {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"  不交换 {arr[j]} 和 {arr[j + 1]}")
        
        print(f"  第 {i + 1} 轮结果: {arr}")
        
        if not swapped:
            print("  数组已有序，提前结束")
            break
    
    return arr


# 测试冒泡排序
if __name__ == "__main__":
    # 测试用例1
    test_array1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 测试用例 1 ===")
    print(f"排序前: {test_array1}")
    sorted_array1 = bubble_sort(test_array1.copy())
    print(f"排序后: {sorted_array1}")
    
    # 测试用例2
    test_array2 = [5, 2, 8, 1, 9]
    print("\n=== 测试用例 2 ===")
    print(f"排序前: {test_array2}")
    sorted_array2 = bubble_sort(test_array2.copy())
    print(f"排序后: {sorted_array2}")
    
    # 测试用例3 - 已排序数组
    test_array3 = [1, 2, 3, 4, 5]
    print("\n=== 测试用例 3 (已排序) ===")
    print(f"排序前: {test_array3}")
    sorted_array3 = bubble_sort(test_array3.copy())
    print(f"排序后: {sorted_array3}")
    
    # 测试用例4 - 带步骤显示
    print("\n=== 带步骤演示 ===")
    demo_array = [64, 34, 25, 12, 22]
    bubble_sort_with_steps(demo_array.copy())