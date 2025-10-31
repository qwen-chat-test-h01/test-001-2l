def bubble_sort(arr):
    """
    冒泡排序算法，带数字类型检查
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    
    异常:
        TypeError: 如果数组中包含非数字元素
    """
    # 检查数组中是否所有元素都是数字
    for item in arr:
        if not isinstance(item, (int, float)):
            raise TypeError(f"数组中包含非数字元素: {item} (类型: {type(item).__name__})")
    
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
    带步骤显示的冒泡排序算法，带数字类型检查
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    # 检查数组中是否所有元素都是数字
    for item in arr:
        if not isinstance(item, (int, float)):
            raise TypeError(f"数组中包含非数字元素: {item} (类型: {type(item).__name__})")
    
    n = len(arr)
    print(f"初始数组: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i+1} 轮排序:")
        
        for j in range(0, n - i - 1):
            print(f"  比较 {arr[j]} 和 {arr[j+1]}", end="")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f" -> 交换: {arr}")
            else:
                print(f" -> 不交换: {arr}")
        
        if not swapped:
            print(f"第 {i+1} 轮没有发生交换，排序完成")
            break
    
    print(f"\n最终结果: {arr}")
    return arr


# 测试冒泡排序
if __name__ == "__main__":
    # 测试正常数字数组
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("测试数组1 (整数):", test_arr1)
    try:
        result1 = bubble_sort(test_arr1.copy())
        print("排序结果:", result1)
    except TypeError as e:
        print("错误:", e)
    
    # 测试包含浮点数的数组
    test_arr2 = [5.5, 2.3, 8.1, 1.0, 9.7]
    print("\n测试数组2 (浮点数):", test_arr2)
    try:
        result2 = bubble_sort(test_arr2.copy())
        print("排序结果:", result2)
    except TypeError as e:
        print("错误:", e)
    
    # 测试包含非数字元素的数组
    test_arr3 = [5, 2, "hello", 1, 9]
    print("\n测试数组3 (包含字符串):", test_arr3)
    try:
        result3 = bubble_sort(test_arr3.copy())
        print("排序结果:", result3)
    except TypeError as e:
        print("错误:", e)
    
    # 测试已排序数组
    test_arr4 = [1, 2, 3, 4, 5]
    print("\n测试数组4 (已排序):", test_arr4)
    try:
        result4 = bubble_sort(test_arr4.copy())
        print("排序结果:", result4)
    except TypeError as e:
        print("错误:", e)
    
    # 测试负数数组
    test_arr5 = [-5, -2, -8, -1, -9]
    print("\n测试数组5 (负数):", test_arr5)
    try:
        result5 = bubble_sort(test_arr5.copy())
        print("排序结果:", result5)
    except TypeError as e:
        print("错误:", e)
    
    # 演示详细排序过程
    print("\n" + "="*50)
    print("演示详细排序过程:")
    demo_arr = [5, 2, 8, 1, 9]
    bubble_sort_with_steps(demo_arr.copy())