def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
    arr: 待排序的列表
    
    返回:
    排序后的列表
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
                print(f"  当前数组: {arr}")
        
        if not swapped:
            print("  没有发生交换，排序完成")
            break
        else:
            print(f"第 {i + 1} 轮结束: {arr}")
    
    print(f"\n最终结果: {arr}")
    return arr


# 测试代码
if __name__ == "__main__":
    # 测试基本功能
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("排序后数组:", sorted_array)
    
    print("\n" + "="*50)
    print("详细排序过程:")
    
    # 显示排序步骤
    test_array2 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_with_steps(test_array2)
    
    # 测试边界情况
    print("\n" + "="*50)
    print("测试边界情况:")
    
    # 空数组
    print("空数组测试:", bubble_sort([]))
    
    # 单个元素
    print("单元素测试:", bubble_sort([42]))
    
    # 已排序数组
    print("已排序数组测试:", bubble_sort([1, 2, 3, 4, 5]))
    
    # 逆序数组
    print("逆序数组测试:", bubble_sort([5, 4, 3, 2, 1]))